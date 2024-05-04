#formulario
from django import forms 
from .models import Topic, Entry, Produto, Saida, ItemSaida#importacao das clases de models.py
#Aqui vc cria as classes do formulario
class TopicForm(forms.ModelForm): #cria classe TopicForm, herda de classe model
    class Meta: #cria classe meta
        model = Topic 
        fields = ['text']
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
        fields = ['categoria', 'marca', 'nome', 'modelo', 'codigo', 'existente', 'sku', 'preco', 'quantidade']



#class 

class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ['observacao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionar um campo de seleção para os itens da saída
        produtos_disponiveis = Produto.objects.filter(existente=True, quantidade__gt=0)
        for produto in produtos_disponiveis:
            self.fields[f'produto_{produto.id}'] = forms.IntegerField(
                label=f'{produto.nome} - Modelo: {produto.modelo}',  # Combine nome e modelo
                min_value=0,
                max_value=produto.quantidade,
                required=False,
                initial=0,
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Salvar a instância principal de saída primeiro, se commit=False
        if not commit:
            instance.save()

        # Salvar os itens de saída
        for field_name, field_value in self.cleaned_data.items():
            if field_name.startswith('produto_') and field_value > 0:
                produto_id = int(field_name.replace('produto_', ''))
                produto = Produto.objects.get(pk=produto_id)
                quantidade = field_value

                # Criar ou atualizar o item de saída
                ItemSaida.objects.update_or_create(
                    saida=instance,
                    produto=produto,
                    defaults={'quantidade': quantidade}
                )

        # Agora salvar a instância principal de saída, se commit=True
        if commit:
            instance.save()

        return instance

class ItemSaidaForm(forms.ModelForm):
    class Meta:
        model = ItemSaida
        fields = ['produto', 'quantidade']