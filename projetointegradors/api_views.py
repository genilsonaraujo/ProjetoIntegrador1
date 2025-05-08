from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Produto, Saida 
from .serializers import ProdutoSerializer, SaidaSerializer 
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class ProdutoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class SaidaList(generics.ListCreateAPIView):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer

    def perform_create(self, serializer):
        saida = serializer.save()  # Salva a saída no banco de dados
        for item in saida.itens.all():  # Itera sobre os itens da saída
            produto = Produto.objects.get(id=item.produto.id)  # Obtém o produto relacionado
            if produto.quantidade >= item.quantidade:  # Verifica se há quantidade suficiente
                produto.quantidade -= item.quantidade  # Decrementa a quantidade do produto
                produto.save()  # Salva as alterações no produto
            else:
                raise ValueError(f"Quantidade de {produto.nome} insuficiente.")  # Levanta erro se não houver estoque

class SaidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer

    def put(self, request, pk):
        saida = self.get_object()
        old_items = {item.produto.id: item.quantidade for item in saida.itens.all()}  # Salva as quantidades antigas
        serializer = self.get_serializer(saida, data=request.data)
        
        if serializer.is_valid():
            # Atualiza a saída antes de ajustar os produtos
            serializer.save()  
            # Atualiza a quantidade de produtos
            for item in serializer.validated_data['itens']:
                produto = Produto.objects.get(id=item['produto'].id)
                quantidade_nova = item['quantidade']
                
                # Verifica se a quantidade mudou e ajusta
                if item['produto'].id in old_items:
                    quantidade_antiga = old_items[item['produto'].id]
                    produto.quantidade += quantidade_antiga  # Reverte a quantidade antiga
                    produto.quantidade -= quantidade_nova  # Decrementa a nova quantidade
                else:
                    produto.quantidade -= quantidade_nova  # Se o item é novo, só decrementa

                produto.save()  # Salva as alterações no produto

            return Response(serializer.data)  # Retorna os dados atualizados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna erros de validação

    def delete(self, request, pk):
        saida = self.get_object()
        for item in saida.itens.all():  # Itera sobre os itens da saída
            produto = Produto.objects.get(id=item.produto.id)  # Obtém o produto relacionado
            produto.quantidade += item.quantidade  # Restaura a quantidade do produto
            produto.save()  # Salva as alterações no produto
        saida.delete()  # Exclui a saída do banco de dados
        return Response(status=status.HTTP_204_NO_CONTENT)  # Retorna resposta 204 No Content
    
def buscar_produto_por_codigo(request, codigo_barras):
    try:
        produto = Produto.objects.get(codigo_barras=codigo_barras)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data, status=200)  # Retorna os detalhes do produto
    except Produto.DoesNotExist:
        return Response({"message": "Produto não encontrado"}, status=404)  # Retorna erro 404 se não existir



class ProdutoBuscaAPIView(APIView):
    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all()
        params = request.query_params

        if params.get('codigo_barras'):
            produtos = produtos.filter(codigo_barras__icontains=params.get('codigo_barras'))
        if params.get('categoria'):
            produtos = produtos.filter(categoria__icontains=params.get('categoria'))
        if params.get('marca'):
            produtos = produtos.filter(marca__icontains=params.get('marca'))
        if params.get('nome'):
            produtos = produtos.filter(nome__icontains=params.get('nome'))
        if params.get('modelo'):
            produtos = produtos.filter(modelo__icontains=params.get('modelo'))
        if params.get('codigo'):
            produtos = produtos.filter(codigo__icontains=params.get('codigo'))
        if params.get('sku'):
            produtos = produtos.filter(sku__icontains=params.get('sku'))
        if params.get('preco_min'):
            produtos = produtos.filter(preco__gte=params.get('preco_min'))
        if params.get('preco_max'):
            produtos = produtos.filter(preco__lte=params.get('preco_max'))

        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



