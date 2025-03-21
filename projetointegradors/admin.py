from django.contrib import admin
from projetointegradors.models import Topic, Entry, Produto #importa a class topic no arquivo models
# Register your models here.
admin.site.register(Topic) #cria topicos
admin.site.register(Entry)
admin.site.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo_barras', 'preco']
    search_fields = ['nome', 'codigo_barras']