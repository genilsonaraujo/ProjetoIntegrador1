from rest_framework import serializers
from .models import Produto, Saida, ItemSaida
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'  # ou especifique os campos manualmente
        #fields = ['nome']


class ItemSaidaSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)  # Adiciona o nome do produto
    class Meta:
        model = ItemSaida
        fields = ['id', 'produto_nome', 'quantidade', 'preco_total']  # Inclua o campo produto_nome

class SaidaSerializer(serializers.ModelSerializer):
    itens = ItemSaidaSerializer(many=True)

    class Meta:
        model = Saida
        fields = ['id', 'data_saida', 'observacao', 'itens']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        saida = Saida.objects.create(**validated_data)
        for item_data in itens_data:
            ItemSaida.objects.create(saida=saida, **item_data)
        return saida