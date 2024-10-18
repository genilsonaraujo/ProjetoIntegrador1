from rest_framework import generics, status
from rest_framework.response import Response
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
        for item in saida.itens.all():
            produto = Produto.objects.get(id=item.produto.id)
            if produto.quantidade >= item.quantidade:
                produto.quantidade -= item.quantidade
                produto.save()
            else:
                raise ValueError(f"Quantidade de {produto.nome} insuficiente.")

class SaidaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer

    def put(self, request, pk):
        saida = self.get_object()
        old_items = {item.produto.id: item.quantidade for item in saida.itens.all()}  # Quantidades antigas
        serializer = self.get_serializer(saida, data=request.data)

        if serializer.is_valid():
            # Restaura as quantidades antigas primeiro
            for item in old_items.keys():
                produto = Produto.objects.get(id=item)
                produto.quantidade += old_items[item]
                produto.save()

            serializer.save()  # Atualiza a saída no banco de dados

            # Atualiza as quantidades com base nos novos itens
            for item in serializer.validated_data['itens']:
                produto = Produto.objects.get(id=item['produto'].id)
                produto.quantidade -= item['quantidade']
                produto.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        saida = self.get_object()
        for item in saida.itens.all():
            produto = Produto.objects.get(id=item.produto.id)
            produto.quantidade += item.quantidade  # Restaura a quantidade do produto
            produto.save()  # Salva a alteração
        saida.delete()  # Exclui a saída
        return Response(status=status.HTTP_204_NO_CONTENT)

