from django.contrib import admin
from django.utils.safestring import mark_safe
from rh.forms import ColaboradorForm, ClienteForm, ProjetoForm
from rh.models import Colaborador, Fornecedores, Cliente, Projeto


class ColaboradorAdmin(admin.ModelAdmin):

    form = ColaboradorForm
    list_display = ("nome", "funcaodobrother", "data_do_nascimento", "thumbnail", "desligado")
    list_filter = ("desligado", )

    def data_do_nascimento(self, obj):
        if obj.data_nascimento:
            return obj.data_nascimento.strftime("%d/%m/%Y")
        return "-"
    data_do_nascimento.short_description = 'Data Nasc.'
    
    def thumbnail(self, obj):
        if obj.foto:
            return mark_safe('<img src="%s" width=100 height=100 />' % obj.foto.url)
        return "-"
    thumbnail.short_description = 'Fotinhoooo'


class FornecedoresAdmin(admin.ModelAdmin):

    list_display = ("titulo", "oque", "quem_indicou")
    list_filter = ("quem_indicou", )


class ClienteAdmin(admin.ModelAdmin):
    
    form = ClienteForm
    list_display = ("nome", "thumbnail", "cnpj", "razaosocial", "nomecontato", "emailcontato", "fonecontato")
    list_filter = ("lidershoot", )

    def thumbnail(self, obj):
        if obj.logo:
            return mark_safe('<img src="%s" width=100 height=100 />' % obj.logo.url)
        return "-"
    thumbnail.short_description = 'Logo'


class ProjetoAdmin(admin.ModelAdmin):
    
    form = ProjetoForm
    list_display = ("nome", "cliente", "numero", "valortotal", "desconto", "valorfinal", "ativismo", "lucro")
    list_filter = ("cliente", )



admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Fornecedores, FornecedoresAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Projeto, ProjetoAdmin)