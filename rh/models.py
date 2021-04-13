from django.db import models


class Colaborador(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome Completo", max_length=100)
    emaildapessoa = models.EmailField("Qual o email do malandro", max_length=200)
    funcaodobrother = models.CharField("Qual a função", max_length=100, blank=True)
    cpf = models.CharField("CPF", max_length=14, blank=True, unique=True)
    data_nascimento = models.DateField("Data de Nascimento", blank=True)
    foto_x = models.PositiveSmallIntegerField("Foto X", default=0, editable=False)
    foto_y = models.PositiveSmallIntegerField("Foto Y", default=0, editable=False)
    foto = models.ImageField(upload_to="colaboradores/fotos", height_field="foto_y", width_field="foto_x", max_length=600, blank=True)
    desligado = models.BooleanField("Desligado?", default=False, db_index=True)

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
    quem_indicou = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Quem indicou?")

    def __str__(self):
        return self.titulo

    class Meta:

        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
