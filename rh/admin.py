from django.contrib import admin
from rh.models import Colaborador, Fornecedores


class ColaboradorAdmin(admin.ModelAdmin):

    list_display = ("nome", "emaildapessoa", "funcaodobrother", "cpf", "data_do_nascimento")

    def data_do_nascimento(self, obj):
        if obj.data_nascimento:
            return obj.data_nascimento.strftime("%d/%m/%Y")
        return "-"
    data_do_nascimento.short_description = 'Data Nasc.'

admin.site.register(Colaborador, ColaboradorAdmin)

class FornecedoresAdmin(admin.ModelAdmin):

    list_display = ("titulo","oque", "datafornecedor")

admin.site.register(Fornecedores, FornecedoresAdmin)
