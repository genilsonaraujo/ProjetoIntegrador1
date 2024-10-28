from django.db import models



# Create your models here.
class Topic(models.Model): #topico tabela no banco de dados
    text = models.CharField(max_length=200)#define quant max de caracteres
    date_added = models.DateTimeField(auto_now_add=True)#herda de models e define horario p/ os dados
    endereco = models.CharField(max_length=255, default='Endereço Padrão')
    cnpj = models.CharField(max_length=14, default='00.000.000/0000-00')
    telefone = models.CharField(max_length=15, default='(00) 0000-0000')
    



    def __str__(self):#define o painel admin, devolve uma representacao do modelo
        """devolve uma representacao """
        return self.text
class Entry(models.Model):#entrando com informacoes para classe Topic
    """algo espefico aprendido (esta em models)"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#chave estrangeira para Topic erdar este modelo relacional
    #esta topic on_delete para que nao apague todo o topico use nulo
    text = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)#erda de models e define horario p/ os dados
class Meta:
    verbose_name_plural = 'entries' #regra de ingles no plural de Entry
def __str__(self):
    """devolve uma string do modelo"""
    return self.text[50] + '...' #quantidade de caracteres


class Produto(models.Model):
    imagem = models.ImageField(
        upload_to='produtos/',
         blank=True, null=True
    )
    
    categoria = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    modelo = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    marca = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default='Sem Marca'
    )
    codigo = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        unique=True)
    existente = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    sku = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        unique=True
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False
    )
    quantidade = models.IntegerField()

def __str__(self):
    return self.name

def editar_produto(self, novo_nome, novo_modelo, nova_marca, nova_categoria, novo_codigo, novo_existente, novo_sku, novo_preco, nova_quantidade):
        # Atualize os campos conforme necessário
        self.nome = novo_nome
        self.modelo = novo_modelo
        self.marca = nova_marca
        self.categoria = nova_categoria
        self.codigo = novo_codigo
        self.existente = novo_existente
        self.sku = novo_sku
        self.preco = novo_preco
        self.quantidade = nova_quantidade

        # Salve as alterações no banco de dados
        self.save()


    
class Saida(models.Model):
    data_saida = models.DateTimeField(auto_now_add=True)
    observacao = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f"Saida #{self.pk}"

class ItemSaida(models.Model):
    saida = models.ForeignKey('Saida', on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Item da Saída #{self.pk}"
