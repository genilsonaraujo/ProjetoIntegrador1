


from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Produto, Saida
from .serializers import ProdutoSerializer, SaidaSerializer
#class ProdutoViewSet(viewsets.ModelViewSet):
    #queryset = Produto.objects.all()
    #serializer_class = ProdutoSerializer
class ProdutoListCreateAPIView(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# ProdutoSerializer está configurado para converter instâncias do modelo Produto em JSON e vice-versa, 
# permitindo a manipulação fácil dos dados na sua API.  Explicação do Código:
#Método get:
#Recupera todos os objetos Produto do banco de dados usando Produto.objects.all().
##Usa o ProdutoSerializer com many=True para serializar vários objetos.
#Retorna a resposta JSON dos produtos serializados.
#Método post:
#Recebe os dados do request e os passa para o ProdutoSerializer para validação.
##Se os dados forem válidos, o serializer chama serializer.save() para criar e salvar um novo objeto Produto.
#Retorna os dados do novo produto criado com status HTTP 201 (Created).
#Se os dados não forem válidos, retorna os erros de validação com status HTTP 400 (Bad Request).


class ProdutoDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Produto.objects.get(pk=pk)
        except Produto.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def put(self, request, pk):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        produto = self.get_object(pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#get(self, request, pk): Obtém um produto específico por id.
#put(self, request, pk): Atualiza completamente um produto (substitui todos os campos).
#patch(self, request, pk): Atualiza parcialmente um produto (modifica apenas os campos fornecidos).
#delete(self, request, pk): Remove o produto específico.
#get_object(self, pk): Método auxiliar para encontrar o produto pelo id, e levanta um Http404 se não for encontrado

#Para  testar os métodos PATCH, PUT, e DELETE no Insomnia ou no Postman usando a URL /produte/<id>/. Por exemplo:

#GET: http://127.0.0.1:8000/produte/1/ (para obter um produto).
#PUT: http://127.0.0.1:8000/produte/1/ (para atualizar completamente o produto).
#PATCH: http://127.0.0.1:8000/produte/1/ (para atualizar parcialmente o produto).
#DELETE: http://127.0.0.1:8000/produte/1/ (para excluir o produto)
class SaidaList(generics.ListCreateAPIView):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer

class SaidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer

    def post(self, request, *args, **kwargs):
        # Use o serializer para validar e criar a saída
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk):
        saida = self.get_object()
        serializer = self.get_serializer(saida)
        return Response(serializer.data)

    def put(self, request, pk):
        saida = self.get_object()
        serializer = self.get_serializer(saida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        saida = self.get_object()
        serializer = self.get_serializer(saida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        saida = self.get_object()
        saida.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
