from django.db import models


class Colaborador(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome Completo", max_length=100)
    emaildapessoa = models.EmailField("Qual o email do malandro", max_length=200)
    funcaodobrother = models.CharField("Qual a função", max_length=100, blank=True)
    cpf = models.CharField("CPF", max_length=14, blank=True, unique=True)
    data_nascimento = models.DateField("Data de Nascimento", blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Colaboradores"
        ordering = ("nome", )


class Fornecedores(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    titulo = models.CharField("Nome do Fornecedor", max_length=100)
    oque = models.CharField("O que faz", max_length=200)
    datafornecedor = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:

        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
