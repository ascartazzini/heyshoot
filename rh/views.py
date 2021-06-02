from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.db.models.base import Model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from rh.forms import ContatoForm
from rh.models import (Atividadecomercial, Biblioteca, CanalProprietario,
                       Certificacao, Cliente, Clima, Colaborador, Contato,
                       Curso, Feedback, Ferramenta, Folguinha, Fornecedores,
                       Hierarquia, Inscricao, Juridico, MomentoImportante,
                       Newsletter, NewsletterTotal, Palestra, Premiacao,
                       Projeto, Promocao, Proposta, ResultadoCanal,
                       TipoProjeto, Workshop)


class IndexView(TemplateView):

    template_name = "index.html"


class BibliotecaView(LoginRequiredMixin, ListView):

    context_object_name = "biblioteca"
    template_name = "biblioteca.html"
    model = Biblioteca


class CanaisProprietariosView(LoginRequiredMixin, ListView):

    context_object_name = "canaisproprietarios"
    template_name = "canais_shoot.html"
    model = CanalProprietario


class CertificacaoView(LoginRequiredMixin, ListView):

    context_object_name = "certificacoes"
    template_name = "certificacoes.html"
    model = Certificacao


class ClienteView(LoginRequiredMixin, ListView):

    context_object_name = "clientes"
    template_name = "clientes.html"
    model = Cliente
    extra_context = {
        "titulo": "Todos os clientes"
    }


class ClienteAtivosView(ClienteView):

    extra_context = {
        "titulo": "Clientes Ativos"
    }

    def get_queryset(self):
        queryset =  super().get_queryset()
        return queryset.filter(proposta__projeto__ativo=True)


class ClienteInativosView(ClienteView):

    extra_context = {
        "titulo": "Clientes Inativos"
    }

    def get_queryset(self):
        queryset =  super().get_queryset()
        return queryset.filter(proposta__projeto__ativo=False)


class ClienteDetalhesView(LoginRequiredMixin, DetailView):

    context_object_name = "cliente"
    template_name = "detalhes_clientes.html"
    model = Cliente


class ClimaView(LoginRequiredMixin, ListView):

    context_object_name = "lista_climas"
    template_name = "clima.html"
    model = Clima


class ClimaDetalhesView(LoginRequiredMixin, DetailView):

    context_object_name = "lista_climas"
    template_name = "detalhes_comunicados.html"
    model = Clima


class ColaboradoresView(LoginRequiredMixin, ListView):

    context_object_name = "colaboradores"
    template_name = "colaboradores.html"
    model = Colaborador


class ColaboradoresDetalhesView(LoginRequiredMixin, DetailView):

    context_object_name = "colaborador"
    template_name = "detalhes_colabs.html"
    model = Colaborador


class ContatoView(LoginRequiredMixin, CreateView):

    model = Contato
    #fields = ["nome", "email", "mensagem"]
    template_name = "contato.html"
    form_class = ContatoForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        messages.success(self.request, "Seu formulário foi enviado. Aguardo o Tuli responder.")
        mensagem = """
            Uma nova pessoa entrou no site e mandou um salve.

            Responder o salve é tão importante quanto não usar drogas.

            Quem Enviou: %s
            Email: %s
            Mensagem: %s

            Assinado.

            Tuli
        """
        nome = form.cleaned_data.get("nome")
        email = form.cleaned_data.get("email")
        mensagem_enviada = form.cleaned_data.get("mensagem")
        mensagem_enviar = mensagem % (nome, email, mensagem_enviada)
        send_mail("Novo Contato no Site",mensagem_enviar, "contato@heyshoot.cc", ["tuli@heyshoot.cc"])
        return super().form_valid(form)


class CursoView(LoginRequiredMixin, ListView):

    context_object_name = "curso"
    template_name = "cursos.html"
    model = Curso


class CursoDetalhesView(LoginRequiredMixin, DetailView):

    context_object_name = "cursos"
    template_name = "detalhes_cursos.html"
    model = Curso


class FeedbackView(LoginRequiredMixin, ListView):

    context_object_name = "feedback"
    template_name = "feedbacks.html"
    model = Feedback


class FeedbackDetalhesView(LoginRequiredMixin, DetailView):

    context_object_name = "feedback"
    template_name = "detalhes_feedback.html"
    model = Feedback


class FerramentaView(LoginRequiredMixin, ListView):

    context_object_name = "ferramentas"
    template_name = "ferramentas.html"
    model = Ferramenta


class FolguinhaView(LoginRequiredMixin, ListView):

    context_object_name = "folguinha"
    template_name = "folgas.html"
    model = Folguinha


class FornecedoresView(LoginRequiredMixin, ListView):

    context_object_name = "fornecedores"
    template_name = "fornecedores.html"
    model = Fornecedores

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["atividades"] = Atividadecomercial.objects.all()
        return context


class FornecedoresDetalhesView(LoginRequiredMixin, DetailView):

    context_object_name = "fornecedores"
    template_name = "detalhes_fornecedores.html"
    model = Fornecedores


class HierarquiaView(LoginRequiredMixin, ListView):

    context_object_name = "hierarquia"
    template_name = "hierarquias.html"
    model = Hierarquia


class InscricaoView(LoginRequiredMixin, ListView):

    context_object_name = "inscricao"
    template_name = "inscricoes.html"
    model = Inscricao


class JuridicoView(LoginRequiredMixin, ListView):

    context_object_name = "juridico"
    template_name = "juridicos.html"
    model = Juridico


class MomentoImportanteView(LoginRequiredMixin, ListView):

    context_object_name = "MomentoImportante"
    template_name = "momentos.html"
    model = MomentoImportante


class NewsletterView(LoginRequiredMixin, ListView):

    context_object_name = "newsletter"
    template_name = "newsletters.html"
    model = Newsletter


class NewsletterTotalView(LoginRequiredMixin, ListView):

    context_object_name = "newslettertotal"
    model = NewsletterTotal


class PalestraView(LoginRequiredMixin, ListView):

    context_object_name = "palestras"
    template_name = "palestras.html"
    model = Palestra


class PremiacaoView(LoginRequiredMixin, ListView):

    context_object_name = "premiacoes"
    template_name = "premiacoes.html"
    model = Premiacao


class ProjetoView(LoginRequiredMixin, ListView):

    context_object_name = "projetos"
    extra_context = {"form_contato": ContatoForm()}
    template_name = "projetos.html"
    model = Projeto


class ProjetoDetalhesView(LoginRequiredMixin, DetailView):

    context_object_name = "projeto"
    template_name = "detalhes_projetos.html"
    model = Projeto


class PromocaoView(LoginRequiredMixin, ListView):

    context_object_name = "promocao"
    template_name = "promocoes.html"
    model = Promocao


class PropostaView(LoginRequiredMixin, ListView):

    context_object_name = "proposta"
    template_name = "propostas.html"
    model = Proposta


class PropostaDetalhesView(LoginRequiredMixin, DetailView):

    context_object_name = "proposta"
    template_name = "detalhes_propostas.html"
    model = Proposta


class ResultadoCanalView(LoginRequiredMixin, ListView):

    context_object_name = "resultadocanal"
    model = ResultadoCanal


class TipoProjetoView(LoginRequiredMixin, ListView):

    context_object_name = "tipoprojeto"
    template_name = "tipo_projeto.html"
    model = TipoProjeto


class WorkshopView(LoginRequiredMixin, ListView):

    context_object_name = "workshop"
    template_name = "workshops.html"
    model = Workshop


class VisaoView(LoginRequiredMixin, TemplateView):

    template_name = "visao.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_inicio = datetime(2021, 1, 1, 0, 0, 0).date()
        data_fim = data_inicio + timedelta(days=365 * 5)
        context["visao"] = {
            "inicio": data_inicio,
            "fim": data_fim,
            "texto": "Vamos ser referência na entrega de impacto social positivo dentro dos mais variados tipos de projeto. Ainda seremos uma empresa de nicho, com uma equipe enxuta e altamente qualificada. Seremos reconhecidos pela forma positiva com que nos relacionamos com as pessoas da empresa, sendo um lugar com baixíssima rotatividade e alto fomento ao crescimento profissional. Nossa atuação será consolidada nos maiores centros brasileiros e também na Europa, com presença constante em premiações ligadas à criatividade para impacto social positivo. Possuiremos diversas certificações ligadas à responsabilidade social e sustentabilidade e teremos sempre uma alta preocupação com sustentabilidade na relação com fornecedores e clientes."
        }
        numero_dias_total = (data_fim - data_inicio).days
        numero_que_ja_passou_de_dias = (data_fim - datetime.now().date()).days
        context["progress_value"] = (numero_dias_total - numero_que_ja_passou_de_dias) / numero_dias_total * 100
        return context


class LoginShootView(LoginView):

    #form_class = LoginForm
    template_name = "login.html"


class LogoutShootView(LogoutView):

    next_page = reverse_lazy("login")
