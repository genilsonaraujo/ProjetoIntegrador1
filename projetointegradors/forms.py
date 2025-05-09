#formulario
from django import forms 
from .models import Topic, Entry, Produto, Saida, ItemSaida#importacao das clases de models.py
#Aqui vc cria as classes do formulario
class TopicForm(forms.ModelForm): #cria classe TopicForm, herda de classe model
    class Meta: #cria classe meta
        model = Topic 
        fields = ['text', 'endereco', 'cnpj', 'telefone']
        labels = {'text': ''}#campo vazio para prenchimento do formulario
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['imagem', 'categoria', 'marca', 'nome', 'modelo','codigo_barras', 'codigo', 'existente', 'sku', 'preco', 'quantidade']



#class 

class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ['observacao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        produtos_disponiveis = Produto.objects.filter(existente=True, quantidade__gt=0)
        self.produtos_dict = {produto.id: produto for produto in produtos_disponiveis}
        
        for produto in produtos_disponiveis:
            self.fields[f'produto_{produto.id}'] = forms.IntegerField(
                label=f'{produto.nome} - Modelo: {produto.modelo} - Codigo: {produto.codigo}',
                min_value=0,
                max_value=produto.quantidade,
                required=False,
                initial=0,
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if not commit:
            instance.save()

        for field_name, quantidade in self.cleaned_data.items():
            if field_name.startswith('produto_') and quantidade > 0:
                produto_id = int(field_name.replace('produto_', ''))
                produto = self.produtos_dict.get(produto_id)

                ItemSaida.objects.update_or_create(
                    saida=instance,
                    produto=produto,
                    defaults={'quantidade': quantidade}
                )

                # Atualiza o estoque
                produto.quantidade -= quantidade
                produto.save()

        if commit:
            instance.save()

        return instance

class ItemSaidaForm(forms.ModelForm):
    class Meta:
        model = ItemSaida
        fields = ['produto', 'quantidade']




class ProdutoSearchForm(forms.Form):
    #query = forms.CharField(label='Buscar produtos', max_length=100)buscar apenas produtos
    codigo_barras = forms.CharField(label='Código de Barras', required=False, max_length=100)
    categoria = forms.CharField(label='Categoria', required=False, max_length=100)
    marca = forms.CharField(label='Marca', required=False, max_length=100)
    nome = forms.CharField(label='Nome', required=False, max_length=100)
    modelo = forms.CharField(label='Modelo', required=False, max_length=100)
    codigo = forms.CharField(label='Código', required=False, max_length=100)
    sku = forms.CharField(label='SKU', required=False, max_length=100)
    preco_min = forms.DecimalField(label='Preço Mínimo', required=False, decimal_places=2, max_digits=10)
    preco_max = forms.DecimalField(label='Preço Máximo', required=False, decimal_places=2, max_digits=10)
    