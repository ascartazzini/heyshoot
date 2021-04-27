from django.db import models


class Colaborador(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
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
    funcaodobrother = models.CharField("Qual a função", max_length=100, blank=True)
    salario = models.CharField("Salário", max_length=200, blank=True)
    desligado = models.BooleanField("Marque aqui se essa pessoa já foi desligada", default=False, db_index=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Colaboradores"
        ordering = ("nome", )
        verbose_name = "a pessoa"



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