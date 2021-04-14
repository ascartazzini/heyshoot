from django.contrib import admin
from django.utils.safestring import mark_safe
from rh.forms import ColaboradorForm
from rh.models import Colaborador, Fornecedores


class ColaboradorAdmin(admin.ModelAdmin):

    form = ColaboradorForm
    list_display = ("nome", "emaildapessoa", "funcaodobrother", "cpf", "data_do_nascimento", "thumbnail", "desligado")
    list_filter = ("desligado", )

    def data_do_nascimento(self, obj):
        if obj.data_nascimento:
            return obj.data_nascimento.strftime("%d/%m/%Y")
        return "-"
    data_do_nascimento.short_description = 'Data Nasc.'

    def thumbnail(self, obj):
        if obj.foto:
            return mark_safe('<img src="%s" />' % obj.foto.url)
        return "-"
    thumbnail.short_description = 'Fotinhoooo'


class FornecedoresAdmin(admin.ModelAdmin):

    list_display = ("titulo", "oque", "quem_indicou")
    list_filter = ("quem_indicou", )


admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Fornecedores, FornecedoresAdmin)
