from django.contrib import admin, messages
from django.contrib.admin.filters import ListFilter
from django.utils.safestring import mark_safe

from rh.forms import (ClienteForm, ClimaForm, ColaboradorForm, CursoForm,
                      PalestraForm, ProjetoForm)
from rh.models import (Atividadecomercial, Biblioteca, CanalProprietario,
                       Certificacao, Cliente, Clima, Colaborador, Contato,
                       Curso, Feedback, Ferramenta, Folguinha, Fornecedores,
                       Hierarquia, Inscricao, Juridico, MomentoImportante,
                       Newsletter, NewsletterTotal, Palestra, Premiacao,
                       Projeto, Promocao, Proposta, ResultadoCanal,
                       TipoProjeto, Visao, Workshop)


class AtividadecomercialAdmin(admin.ModelAdmin):

    list_display = ("nome", "desc")


class BibliotecaAdmin(admin.ModelAdmin):

    list_display = ("titulo", "recomendado", "autor", "thumbnail")
    list_filter = ("titulo", )

    def thumbnail(self, obj):
        if obj.imagem:
            return mark_safe('<img src="%s" width=100 height=100 />' % obj.imagem.url)
        return "-"
    thumbnail.short_description = 'Imagem'


class CanalProprietarioAdmin(admin.ModelAdmin):

    list_display = ("nome", "link")
    list_filter = ("nome", )


class CertificacaoAdmin(admin.ModelAdmin):

    list_display = ("nome", "desc", "thumbnail", "preco", "quando")
    
    def thumbnail(self, obj):
        if obj.selo:
            return mark_safe('<img src="%s" width=100 height=100 />' % obj.selo.url)
        return "-"
    thumbnail.short_description = 'Selo'


class ClienteAdmin(admin.ModelAdmin):

    form = ClienteForm
    list_display = ("nome", "thumbnail", "cnpj", "razaosocial", "nomecontato", "emailcontato", "fonecontato")
    search_fields = ("nome", )

    def thumbnail(self, obj):
        if obj.logo:
            return mark_safe('<img src="%s" width=100 height=100 />' % obj.logo.url)
        return "-"
    thumbnail.short_description = 'Logo'


class ClimaAdmin(admin.ModelAdmin):
    
    form = ClimaForm
    list_display = ("nome", "desc", "quando")
    list_filter = ("nome", )
    search_fields = ("nome", )


class ContatoAdmin(admin.ModelAdmin):

    list_display = ("nome","email", "mensagem")
    list_filter = ("nome", )


class CursoAdmin(admin.ModelAdmin):

    form = CursoForm
    list_display = ("qual", "quando", "verba")
    list_filter = ("paraquem", )
    search_fields = ("paraquem", )


class FeedbackAdmin(admin.ModelAdmin):

    list_display = ("quando", "comquem", "analise")
    list_filter = ("comquem", )
    search_fields = ("analise", )


class FerramentaAdmin(admin.ModelAdmin):

    list_display = ("nome","quando", "preco", "user", "senha")
    list_filter = ("preco", "nome")


class FolguinhaAdmin(admin.ModelAdmin):

    list_display = ("quem", "inicio", "fim")
    list_filter = ("quem", )


class FornecedoresAdmin(admin.ModelAdmin):

    list_display = ("titulo", "email", "cidade", "observ", "atividade", "iniciativanaobranca","sustentavel")
    list_filter = ("atividade", "iniciativanaobranca", "sustentavel" )
    search_fields = ("titulo", )


class HierarquiaAdmin(admin.ModelAdmin):

    list_display = ("nome", "salariomin", "salariomax")
    list_filter = ("nome", )


class InscricaoAdmin(admin.ModelAdmin):

    list_display = ("premio", "projeto", "categoria", "posicao", "quando")


class JuridicoAdmin(admin.ModelAdmin):

    list_display = ("nome", "desc", "prop")


class MomentoImportanteAdmin(admin.ModelAdmin):

    list_display = ("nome", "quem", "desc", "quando")


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ("nome", "objetivo")


class NewsletterTotalAdmin(admin.ModelAdmin):
    
    list_display = ("news", "quando", "inscritos")


class PalestraAdmin(admin.ModelAdmin):

    form = PalestraForm    
    list_display = ("nome", "desc")


class PremiacaoAdmin(admin.ModelAdmin):

    list_display = ("nome","desc","periodo","investimento")


class ProjetoAdmin(admin.ModelAdmin):

    form = ProjetoForm
    list_display = ("nome","numero", "cliente", "lider_shoot", "ativo")
    list_filter = ("numero", "ativo")


class ProjetoInlineAdmin(admin.TabularInline):

    model = Projeto
    extra = 1


class ColaboradorAdmin(admin.ModelAdmin):

    inlines = [ProjetoInlineAdmin]
    form = ColaboradorForm
    list_display = ("nome", "funcaodobrother", "data_do_nascimento", "thumbnail", "entrounashoot" , "desligado")
    list_filter = ("desligado", )
    search_fields = ("nome", )

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

class PromocaoAdmin(admin.ModelAdmin):

    list_display = ("quem", "quando", "paraqual")
    list_filter = ("quem", )
    search_fields = ("quem", )

    def save_model(self, request, obj, form, change):
        r = super().save_model(request, obj, form, change)
        obj.quem.funcaodobrother = obj.paraqual
        obj.quem.save()
        messages.success(request, "O colaborador teve o seu status alterado.")
        return r


class PropostaAdmin(admin.ModelAdmin):

    list_display = ("nome", "cliente", "numero", "valor_final", "lucro", "ativismo", "horas", "tipoprojeto")
    list_filter = ("cliente", )
    search_fields = ("nome", )


class ResultadoCanalAdmin(admin.ModelAdmin):

    list_display = ("canal", "base", "engajamento", "quando")
    list_filter = ("canal", "engajamento")


class TipoProjetoAdmin(admin.ModelAdmin):

    list_display = ("nome", "descri", "tempo")
    list_filter = ("tempo", )
    

class WorkshopAdmin(admin.ModelAdmin):

    list_display = ("titulo", "objetivos")
    list_filter = ("titulo", )


class VisaoAdmin(admin.ModelAdmin):

    list_display = ("inicio","fim","texto")
        



admin.site.register(Atividadecomercial, AtividadecomercialAdmin)
admin.site.register(Biblioteca, BibliotecaAdmin)
admin.site.register(CanalProprietario, CanalProprietarioAdmin)
admin.site.register(Certificacao, CertificacaoAdmin)
admin.site.register(Clima, ClimaAdmin)
admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Folguinha, FolguinhaAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Ferramenta, FerramentaAdmin)
admin.site.register(Fornecedores, FornecedoresAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(MomentoImportante, MomentoImportanteAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(NewsletterTotal, NewsletterTotalAdmin)
admin.site.register(Hierarquia, HierarquiaAdmin)
admin.site.register(Inscricao, InscricaoAdmin)
admin.site.register(Juridico, JuridicoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Proposta, PropostaAdmin)
admin.site.register(TipoProjeto, TipoProjetoAdmin)
admin.site.register(Palestra, PalestraAdmin)
admin.site.register(Premiacao, PremiacaoAdmin)
admin.site.register(Promocao, PromocaoAdmin)
admin.site.register(ResultadoCanal, ResultadoCanalAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Visao, VisaoAdmin)
