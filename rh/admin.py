from django.contrib import admin
from django.utils.safestring import mark_safe

from rh.forms import (ClienteForm, ClimaForm, ColaboradorForm, CursoForm,
                      ProjetoForm)
from rh.models import (Atividadecomercial, Cliente, Clima, Colaborador,
                       Contato, Curso, Folguinha, Fornecedores, Hierarquia,
                       Projeto, Proposta, TipoProjeto)


class AtividadecomercialAdmin(admin.ModelAdmin):

    list_display = ("nome", "desc")


class ColaboradorAdmin(admin.ModelAdmin):

    form = ColaboradorForm
    list_display = ("nome", "funcaodobrother", "data_do_nascimento", "thumbnail", "entrounashoot" , "desligado")
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
    thumbnail.short_description = 'Foto'


class FolguinhaAdmin(admin.ModelAdmin):

    list_display = ("quem", "inicio", "fim")
    list_filter = ("quem", )


class FornecedoresAdmin(admin.ModelAdmin):

    list_display = ("titulo", "email", "cidade", "observ", "atividade", "iniciativanaobranca")
    list_filter = ("atividade", "iniciativanaobranca", )


class ClienteAdmin(admin.ModelAdmin):

    form = ClienteForm
    list_display = ("nome", "thumbnail", "cnpj", "razaosocial", "nomecontato", "emailcontato", "fonecontato")
    list_filter = ("lider_shoot", )

    def thumbnail(self, obj):
        if obj.logo:
            return mark_safe('<img src="%s" width=100 height=100 />' % obj.logo.url)
        return "-"
    thumbnail.short_description = 'Logo'


class HierarquiaAdmin(admin.ModelAdmin):

    list_display = ("nome", "salariomin", "salariomax")
    list_filter = ("nome", )


class PropostaAdmin(admin.ModelAdmin):

    list_display = ("nome", "cliente", "numero", "valor_final", "lucro", "ativismo", "horas", "tipoprojeto")
    list_filter = ("cliente", )


class ProjetoAdmin(admin.ModelAdmin):

    form = ProjetoForm
    list_display = ("nome","numero", "lider_shoot")
    list_filter = ("numero", )

class ContatoAdmin(admin.ModelAdmin):
    
    list_display = ("nome","email", "mensagem")
    list_filter = ("nome", )


class TipoProjetoAdmin(admin.ModelAdmin):

    list_display = ("nome", "descri", "tempo")
    list_filter = ("tempo", )


class ClimaAdmin(admin.ModelAdmin):
    
    form = ClimaForm
    list_display = ("nome", "desc")
    list_filter = ("nome", )
    

class CursoAdmin(admin.ModelAdmin):
    
    form = CursoForm
    list_display = ("qual", "quando")
    list_filter = ("paraquem", )
    

admin.site.register(Atividadecomercial, AtividadecomercialAdmin)
admin.site.register(Clima, ClimaAdmin)
admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Folguinha, FolguinhaAdmin)
admin.site.register(Fornecedores, FornecedoresAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Hierarquia, HierarquiaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Proposta, PropostaAdmin)
admin.site.register(TipoProjeto, TipoProjetoAdmin)
