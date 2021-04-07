from django.db import models


class Colaborador(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome Completo", max_length=100)
    cpf = models.CharField("CPF", max_length=14, blank=True, unique=True)
    data_nascimento = models.DateField("Data de Nascimento", blank=True)
    eh_negra = models.BooleanField("É uma pessoa negra?", db_index=True, default=False)

    def __str__(self):
        return self.nome

    class Meta:

        verbose_name_plural = "Colaboradores"
        ordering = ("nome", )
