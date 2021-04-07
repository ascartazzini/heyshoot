from django.contrib import admin
from rh.models import Colaborador


class ColaboradorAdmin(admin.ModelAdmin):

    list_display = ("nome", "id", "cpf", "data_nascimento", "eh_negra")
    list_filter = ("eh_negra", )


admin.site.register(Colaborador, ColaboradorAdmin)
