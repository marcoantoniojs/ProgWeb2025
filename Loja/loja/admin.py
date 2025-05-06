from django.contrib import admin #isso já vai estar existindo no arquivo
# Register your models here.
from .models import * #imporata nossos models

class FabricanteAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
    fields = ('Produto', 'destaque', 'promocao', 'preco', 'categoria',) #'msgPromocao' foi tirado pois não se usa fields e exclude ao mesmo tempo
    search_fields = ('Produto',)
    exclude = ('msgPromocao',)


admin.site.register(Fabricante,FabricanteAdmin) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)