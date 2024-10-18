from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Produto, Saida
from .serializers import ProdutoSerializer, SaidaSerializer
from django.http import Http404

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




