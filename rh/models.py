from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model


class Atividadecomercial(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Qual a atividade Comercial", max_length=100, blank=True)
    desc = models.CharField("Alguma descrição?", max_length=100, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Atividade"



class Hierarquia(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome da Função", max_length=200, blank=True)
    salariomin = models.DecimalField("Salário mínimo", max_digits=9, decimal_places=2, blank=True, null=True)
    salariomax = models.DecimalField("Salário máximo", max_digits=9, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome


class Colaborador(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, null=True, blank=True, verbose_name="Usuário no sistema", on_delete=models.PROTECT)
    nome = models.CharField("Nome completo", max_length=100)
    data_nascimento = models.DateField("Data de nascimento", blank=True, null=True)
    cpf = models.CharField("CPF", max_length=14, blank=True, unique=True)
    cpffile = models.FileField("Foto do CPF", upload_to="colaboradores/docs", max_length=600, blank=True)
    errege = models.CharField("RG", max_length=14, blank=True)
    rgfile = models.FileField("Foto do RG", upload_to="colaboradores/docs", max_length=600, blank=True)
    endereco = models.CharField("Endereço", max_length=200, blank=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True)
    estado = models.CharField("Estado", max_length=100, blank=True)
    pais = models.CharField("País", max_length=200, blank=True)
    telefone = models.CharField("Fone", max_length=200, blank=True)
    banco = models.CharField("Banco", max_length=200, blank=True)
    conta = models.CharField("Conta", max_length=200, blank=True)
    emailpessoal = models.EmailField("Qual o email pessoal", max_length=200, blank=True)
    emailshoot = models.EmailField("Qual o email da Shoot", max_length=200, blank=True)
    foto_x = models.PositiveSmallIntegerField("Foto X", default=0, editable=False)
    foto_y = models.PositiveSmallIntegerField("Foto Y", default=0, editable=False)
    foto = models.ImageField(upload_to="colaboradores/fotos", height_field="foto_y", width_field="foto_x", max_length=600, blank=True)
    funcaodobrother = models.ForeignKey(Hierarquia, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Qual a função atual")
    salario = models.CharField("Salário", max_length=200, blank=True)
    entrounashoot = models.DateField("Entrou na Shoot que dia", blank=True, null=True)
    desligado = models.BooleanField("Não trampa mais aqui?", default=False, db_index=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Colaboradores"
        ordering = ("nome", )
        verbose_name = "a pessoa"


class Folguinha(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    quem = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Quem")
    inicio = models.DateField("De quando", blank=True, null=True)
    fim = models.DateField("Até quando", blank=True, null=True)

    class Meta:
        verbose_name = "Folguinha"


class Fornecedores(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    titulo = models.CharField("Empresa", max_length=100, blank=True)
    oque = models.CharField("Contato", max_length=200, blank=True)
    fone = models.CharField("Fone", max_length=100, blank=True)
    email = models.CharField("Email", max_length=200, blank=True)
    cidade = models.CharField("Cidade", max_length=200, blank=True)
    observ = models.CharField("Observação", max_length=200, blank=True)
    quem_indicou = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Quem indicou?")
    atividade = models.ForeignKey(Atividadecomercial, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Atividade")
    iniciativanaobranca = models.BooleanField("Iniciativa não-branca", default=False, db_index=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"


class Cliente(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Empresa", max_length=100)
    cnpj = models.CharField("CNPJ", max_length=18, blank=True)
    razaosocial = models.CharField("Razão Social", max_length=200, blank=True)
    foto_x = models.PositiveSmallIntegerField("Foto X", default=0, editable=False)
    foto_y = models.PositiveSmallIntegerField("Foto Y", default=0, editable=False)
    logo = models.ImageField(upload_to="clientes/logos", height_field="foto_y", width_field="foto_x", max_length=600, blank=True)
    nomecontato = models.CharField("Líder no cliente", max_length=200, blank=True)
    emailcontato = models.CharField("E-mail de contato", max_length=200, blank=True)
    fonecontato = models.CharField("Fone do contato", max_length=200, blank=True)
    lider_shoot = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Líder Shoot")

    def __str__(self):
        return self.nome


class Projeto(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome do Projeto", max_length=100, blank=True)
    numero = models.IntegerField("Número da Proposta", blank=True)
    lider_shoot = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Líder Shoot", related_name="lider")
    colaboradores = models.ManyToManyField(Colaborador, blank=True)
    resumo = models.TextField("Um breve resumo do projeto", help_text="Este campo é utilizado na apresentação dos detalhes do projeto no nosso site.", blank=True, default='')

    def __str__(self):
        return self.nome


class TipoProjeto(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome", max_length=100, blank=True)
    descri = models.CharField("Descrição", max_length=600, blank=True)
    tempo = models.IntegerField("Tempo do processo", blank=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Projeto"


class Proposta(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome do Projeto", max_length=100, blank=True)
    numero = models.IntegerField("Número da Proposta", blank=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Cliente")
    tipoprojeto = models.ForeignKey(TipoProjeto, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Tipo")
    # Quando for utilizar dinheiro, ou alguma coisa que tenha um número de casas decimais fixas (por exemplo duas)
    # pode-se utilizar o campo "DecimalField". max_digitas é o tamanho total do campo, e o decimal_places são o número de
    # casas que o número terá depois da ","
    valor_final = models.DecimalField("Valor final", max_digits=9, decimal_places=2, blank=True, null=True)
    lucro = models.IntegerField("Lucro da Shoot", blank=True, null=True)
    ativismo = models.IntegerField("Quanto pra ativismo", blank=True, null=True)
    horas = models.IntegerField("Horas vendidas", blank=True, null=True)

    def __str__(self):
        return self.nome


class Contato(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-mail")
    mensagem = models.TextField("Mensagem")

    def __str__(self):
        return "%s: %s" % (self.nome, self.email)


class Clima(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome da Pesquisa de Clima", max_length=200, blank=True)
    desc = models.CharField("Descrição da pesquisa", max_length=200, blank=True)
    quando = models.DateField("Aplicou quando", blank=True, null=True)
    paraquem = models.ManyToManyField(Colaborador, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pesquisas de clima"


class Curso(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    quando = models.DateField("Quando", blank=True, null=True)
    qual = models.CharField("Qual curso foi?", max_length=200, blank=True)
    paraquem = models.ForeignKey(Colaborador, verbose_name="Para quem", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Curso"


class Promocao(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    quem = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Para quem")
    quando = models.DateField("Quando", blank=True, null=True)
    paraqual = models.ForeignKey(Hierarquia, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Para o que")

    class Meta:
        verbose_name = "Promoção"
        verbose_name_plural = "Promoções"
