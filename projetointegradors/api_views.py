from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Produto, Saida, ItemSaida
from .serializers import ProdutoSerializer, SaidaSerializer

class ProdutoListCreateAPIView(APIView):
    def get(self, request):
        # Recupera todos os produtos do banco de dados
        produtos = Produto.objects.all()
        # Serializa a lista de produtos
        serializer = ProdutoSerializer(produtos, many=True)
        # Retorna os produtos serializados como resposta
        return Response(serializer.data)

    def post(self, request):
        # Valida os dados recebidos para criar um novo produto
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Salva o novo produto no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna o produto criado
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna erros de validação

class ProdutoDetailAPIView(APIView):
    def get_object(self, pk):
        # Método auxiliar para obter um produto pelo ID
        try:
            return Produto.objects.get(pk=pk)
        except Produto.DoesNotExist:
            raise Http404  # Levanta um erro 404 se o produto não for encontrado

    def get(self, request, pk):
        # Obtém um produto específico
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)  # Retorna os dados do produto

    def put(self, request, pk):
        # Atualiza completamente um produto
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Salva as alterações no produto
            return Response(serializer.data)  # Retorna os dados atualizados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna erros de validação

    def patch(self, request, pk):
        # Atualiza parcialmente um produto
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Salva as alterações no produto
            return Response(serializer.data)  # Retorna os dados atualizados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna erros de validação

    def delete(self, request, pk):
        # Remove um produto específico
        produto = self.get_object(pk)
        produto.delete()  # Exclui o produto do banco de dados
        return Response(status=status.HTTP_204_NO_CONTENT)  # Retorna resposta 204 No Content

class SaidaList(generics.ListCreateAPIView):
    queryset = Saida.objects.all()  # Define a queryset para saídas
    serializer_class = SaidaSerializer  # Define o serializer para a saída

    def perform_create(self, serializer):
        # Método chamado quando uma saída é criada
        saida = serializer.save()  # Salva a saída no banco de dados
        # Atualiza o estoque dos produtos relacionados
        for item in saida.itens.all():
            produto = Produto.objects.get(id=item.produto.id)  # Obtém o produto relacionado
            produto.quantidade -= item.quantidade  # Decrementa a quantidade do produto
            produto.save()  # Salva as alterações no produto

class SaidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saida.objects.all()  # Define a queryset para saídas
    serializer_class = SaidaSerializer  # Define o serializer para a saída

    def get(self, request, pk):
        # Obtém uma saída específica
        saida = self.get_object()
        serializer = self.get_serializer(saida)
        return Response(serializer.data)  # Retorna os dados da saída

    def put(self, request, pk):
        # Atualiza completamente uma saída
        saida = self.get_object()
        serializer = self.get_serializer(saida, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Salva as alterações na saída
            return Response(serializer.data)  # Retorna os dados atualizados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna erros de validação

    def patch(self, request, pk):
        # Atualiza parcialmente uma saída
        saida = self.get_object()
        serializer = self.get_serializer(saida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Salva as alterações na saída
            return Response(serializer.data)  # Retorna os dados atualizados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Retorna erros de validação

    def delete(self, request, pk):
        # Remove uma saída específica
        saida = self.get_object()
        saida.delete()  # Exclui a saída do banco de dados
        return Response(status=status.HTTP_204_NO_CONTENT)  # Retorna resposta 204 No Content



