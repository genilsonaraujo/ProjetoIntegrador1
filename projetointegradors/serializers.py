from rest_framework import serializers
from .models import Produto, Saida, ItemSaida

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ItemSaidaSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)

    class Meta:
        model = ItemSaida
        fields = ['id', 'produto', 'produto_nome', 'quantidade', 'preco_total']

    def create(self, validated_data):
        # Supondo que o produto está incluído nos dados validados
        produto = validated_data['produto']
        quantidade = validated_data['quantidade']
        # Calcule o preço total
        validated_data['preco_total'] = produto.preco * quantidade  # Substitua 'preco' pelo campo correto no seu modelo
        return super().create(validated_data)

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
