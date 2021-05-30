from django.contrib.auth.models import User
from django.db import models
from django.db.models import base
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, DateTimeField
from django.db.models.fields.related import ForeignKey



class Atividadecomercial(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Qual a atividade Comercial", max_length=100, blank=True)
    desc = models.CharField("Alguma descrição?", max_length=100, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Atividade"


class CanalProprietario(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome do Canal", max_length=100, blank=True)
    objetivo = models.TextField("Objetivo do canal", blank=True)
    link = models.CharField("Link do canal", max_length=200, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Canais Proprietários"


class Certificacao(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome da certificação", blank=True, max_length=150)
    selo_x = models.PositiveSmallIntegerField("Selo X", default=0, editable=False)
    selo_y = models.PositiveSmallIntegerField("Selo Y", default=0, editable=False)
    selo = models.ImageField(upload_to="certificacoes/logos", height_field="selo_y", width_field="selo_x", max_length=600, blank=True)
    desc = models.TextField("Descrição da certificação", blank=True)
    preco = models.DecimalField("Investimento", blank=True, max_digits=9, decimal_places=2, null=True)
    quando = DateField("Quando certificamos", blank=True, null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Certificação"
        verbose_name_plural = "Certificações"


class Contato(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-mail")
    mensagem = models.TextField("Mensagem")

    def __str__(self):
        return "%s: %s" % (self.nome, self.email)


class Ferramenta(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    updater = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome da ferramenta", blank=True, max_length=100, null=True)
    desc = models.TextField("Descrição", blank=True, null=True)
    quando = models.DateField("Início da assinatura", blank=True, null=True)
    preco = models.DecimalField("Investimento anual", blank=True, max_digits=9, decimal_places=2, null=True)
    user = models.CharField("User", blank=True, null=True, max_length=100)
    senha = models.CharField("Pass", blank=True, null=True, max_length=100)
    
    def __str__(self):
        return self.nome


class Hierarquia(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome da Função", max_length=200, blank=True)
    salariomin = models.DecimalField("Salário mínimo", max_digits=9, decimal_places=2, blank=True, null=True)
    salariomax = models.DecimalField("Salário máximo", max_digits=9, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome


class MomentoImportante(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome do momento", max_length=100, null=True, blank=True)
    quem = models.CharField("Pessoa/Cliente/Parceiro", max_length=100, null=True, blank=True)
    quando = models.DateField("Data", blank=True, null=True)
    desc = models.TextField("Descrição", null=True)

    def __str__(self):
        return self.nome


class Newsletter(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updater = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome da base", blank=True, max_length=100, null=True)
    objetivo = models.TextField("Objetivo da base", blank=True, null=True)
    
    def __str__(self):
        return self.nome


class NewsletterTotal(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updater = models.DateTimeField(auto_now=True)
    news = models.ForeignKey(Newsletter, null=True, on_delete=models.SET_NULL, verbose_name="Base")
    quando = models.DateField("Quando", blank=True, null=True)
    inscritos = models.IntegerField("Inscritos", blank=True)

    def __str__(self):
        return "%s" % (self.news)

    class Meta:
        verbose_name = "Resultados Newsletter"
        

class Premiacao(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome da premiação", blank=True, max_length=100)
    site = models.CharField("Link do site", blank=True, max_length=100)
    desc = models.TextField("Descrição da premiação", blank=True)
    periodo = models.CharField("Período de inscrição", blank=True, max_length=100)
    categorias = models.CharField("Categorias interessantes", max_length=200, blank=False)
    investimento = models.DecimalField("Investimento médio", max_digits=9, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Premiação"
        verbose_name_plural = "Premiações"


class ResultadoCanal(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    base = models.IntegerField("Número total de base", blank=True)
    engajamento = models.DecimalField("Engajamento do canal", max_digits=4, decimal_places=2, blank=True, null=True)
    quando = DateField("Informação do dia", blank=True, null=True)
    canal = models.ForeignKey(CanalProprietario, null=True, on_delete=models.SET_NULL, verbose_name="Canal")

    def __str__(self):
        return "%s" % (self.canal)


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


class Workshop(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    titulo = models.CharField("Qual o título do workshop?", blank=True, max_length=100)
    desc = models.TextField("Breve descrição", blank=True)
    objetivos = models.CharField("Quais os objetivos contemplados", blank=True, max_length=200)
    roteiro = models.TextField("Qual o roteiro/metodologia", blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Workshops"


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
    bairro = models.CharField("Bairro", max_length=200, blank=True, null=True)
    cep = models.CharField("CEP", max_length=200, blank=True, null=True)
    cidade = models.CharField("Cidade", max_length=100, blank=True)
    estado = models.CharField("Estado", max_length=100, blank=True)
    pais = models.CharField("País", max_length=200, blank=True)
    telefone = models.CharField("Fone", max_length=200, blank=True)
    agencia = models.CharField("Agência", max_length=200, blank=True, null=True)
    banco = models.CharField("Banco", max_length=200, blank=True)
    conta = models.CharField("Conta", max_length=200, blank=True)
    emailpessoal = models.EmailField("Qual o email pessoal", max_length=200, blank=True)
    emailshoot = models.EmailField("Qual o email da Shoot", max_length=200, blank=True)
    foto_x = models.PositiveSmallIntegerField("Foto X", default=0, editable=False)
    foto_y = models.PositiveSmallIntegerField("Foto Y", default=0, editable=False)
    foto = models.ImageField(upload_to="colaboradores/fotos", height_field="foto_y", width_field="foto_x", max_length=600, blank=True)
    funcaodobrother = models.ForeignKey(Hierarquia, null=True, on_delete=models.SET_NULL, verbose_name="Qual a função atual")
    salario = models.CharField("Salário", max_length=200, blank=True)
    bio = models.TextField("Mini bio", null=True)
    instagram = models.CharField("Instagram", max_length=100, blank=True)
    linkedin = models.CharField("Linkedin", max_length=100, blank=True)
    facebook = models.CharField("Facebook", max_length=100, blank=True)
    entrounashoot = models.DateField("Entrou na Shoot que dia", blank=True, null=True)
    desligado = models.BooleanField("Não trampa mais aqui?", default=False, db_index=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Colaboradores"
        ordering = ("nome", )
        verbose_name = "a pessoa"



class Biblioteca(models.Model):

        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        titulo = models.CharField("Título do livro", max_length=100, blank=True, null=True)
        recomendado = ForeignKey(Colaborador, null=True, on_delete=models.SET_NULL, verbose_name="Recomendado Por")
        autor = models.CharField("Autor", max_length=100)
        desc = models.TextField("Porque você recomenda", null=True)
        imagem_x = models.PositiveSmallIntegerField("Imagem X", default=0, editable=False)
        imagem_y = models.PositiveSmallIntegerField("Imagem Y", default=0, editable=False)
        imagem = models.ImageField(upload_to="bibilioteca/imagens", height_field="imagem_y", width_field="imagem_x", max_length=600, blank=True)

        def __str__(self):
            return self.titulo


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
    inicio = models.DateField("Início da relação", blank=True, null=True)
    fim = models.DateField("Fim da relação", blank=True, null=True)

    def __str__(self):
        return self.nome


class Clima(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome do documento para leitura", max_length=200, blank=True)
    desc = models.TextField("Descrição do que é", max_length=200, blank=True)
    quando = models.DateField("Quando foi enviado", blank=True, null=True)
    paraquem = models.ManyToManyField(Colaborador, blank=True, verbose_name="Quem confirmou leitura:")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Comunicados oficiais"
        ordering = ['-quando']


class Curso(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    quando = models.DateField("Quando", blank=True, null=True)
    qual = models.CharField("Qual curso foi?", max_length=200, blank=True)
    verba = models.DecimalField("Verba", max_digits=9, decimal_places=2, blank=True, null=True)
    paraquem = models.ForeignKey(Colaborador, verbose_name="Para quem", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.paraquem)

    class Meta:
        verbose_name = "Curso"


class Feedback(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    quando = models.DateField("Quando", blank=True, null=True)
    comquem = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Com quem" )
    analise = models.TextField("Análise feita", max_length=200, blank=True)

    def __str__(self):
        return "%s" % (self.comquem)

    class Meta:
        verbose_name_plural = "Feedbacks"


class Folguinha(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    quem = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Quem")
    inicio = models.DateField("De quando", blank=True, null=True)
    fim = models.DateField("Até quando", blank=True, null=True)

    def __str__(self):
        return str(self.quem)

    class Meta:
        verbose_name_plural = "Férias e folgas"


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
    sustentavel = models.BooleanField("Iniciativa sustentável", default=False, db_index=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"


class Palestra(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    updater = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome da Palestra", max_length=150, blank=True)
    desc = models.TextField("Descrição da palestra", blank=True)
    quem = models.ManyToManyField(Colaborador, blank=True, verbose_name="Quem é capaz de dar essa palestra")

    def __str__(self):
        return self.nome


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


class Projeto(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome do Projeto", max_length=100, blank=True)
    numero = models.ForeignKey(Proposta, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Proposta")
    # numero = models.IntegerField("Número da Proposta", blank=True)
    data_inicio = models.DateField("Data de Início", blank=True, null=True)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.PROTECT, verbose_name="Cliente")
    lider_shoot = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Líder Shoot", related_name="lider")
    colaboradores = models.ManyToManyField(Colaborador, blank=True)
    resumo = models.TextField("Um breve resumo do projeto", help_text="Este campo é utilizado na apresentação dos detalhes do projeto no nosso site.", blank=True, default='')
    # DB Index informa o banco de dados para fazer um índice sobre a coluna
    # na qual será utilizada para fazer consultas. É uma maneira de otimizar
    # o sistema.
    ativo = models.BooleanField("Está ativo?", db_index=True, default=False)

    def __str__(self):
        return self.nome


class Promocao(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    quem = models.ForeignKey(Colaborador, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Para quem")
    quando = models.DateField("Quando", blank=True, null=True)
    paraqual = models.ForeignKey(Hierarquia, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Para o que")

    def __str__(self):
        return "%s | %s" % (self.quem, self.paraqual)

    class Meta:
        verbose_name = "Promoção"
        verbose_name_plural = "Promoções"


class Juridico(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    nome = models.CharField("Nome do documento", max_length=200, blank=True)
    urldoc = models.CharField("URL do doc", max_length=200, blank=True)
    desc = models.TextField("Pra que serve", blank=True, null=True)
    prop = models.ForeignKey(Proposta, null=True, on_delete=models.SET_NULL, verbose_name="Proposta")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Docs Jurídicos"


class Inscricao(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    premio = models.ForeignKey(Premiacao, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Qual Prêmio")
    projeto = models.ForeignKey(Projeto, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Projeto inscrito")
    categoria = models.CharField("Categoria que concorremos", blank=True, max_length=200)
    posicao = models.CharField("Posição final", blank=True, max_length=200)
    investimento = models.DecimalField("Investimento", max_digits=9, decimal_places=2, blank=True, null=True)
    quando = models.DateField("Quando", blank=True, null=True)

    def __str__(self):
        return "%s" % (self.premio)

    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"


class Visao(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    inicio = DateField("Lançado dia", blank=True, null=True)
    fim = DateField("Valido até dia", blank=True, null=True)
    texto = models.TextField("Visão", blank=True, null=True)

    def __str__(self):
        return "Visão"

    class Meta:
        verbose_name_plural = "Visão"