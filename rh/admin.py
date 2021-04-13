from django.contrib import admin
from rh.models import Colaborador, Fornecedores


class ColaboradorAdmin(admin.ModelAdmin):

    list_display = ("nome", "emaildapessoa", "funcaodobrother", "cpf", "data_nascimento")

admin.site.register(Colaborador, ColaboradorAdmin)

class FornecedoresAdmin(admin.ModelAdmin):
    
    list_display = ("titulo","oque", "datafornecedor")

admin.site.register(Fornecedores, FornecedoresAdmin)
