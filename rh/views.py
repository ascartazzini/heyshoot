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


class BibliotecaView(ListView):

    context_object_name = "biblioteca"
    template_name = "biblioteca.html"
    model = Biblioteca


class CanaisProprietariosView(ListView):

    context_object_name = "canaisproprietarios"
    template_name = "canais_shoot.html"
    model = CanalProprietario


class CertificacaoView(ListView):

    context_object_name = "certificacoes"
    template_name = "certificacoes.html"
    model = Certificacao


class ClienteView(ListView):

    context_object_name = "clientes"
    template_name = "clientes.html"
    model = Cliente
    # TODO: Como fazer tudo na mesma view


class ClienteAtivosView(ClienteView):

    template_name = "clientes-ativos.html"

    def get_queryset(self):
        queryset =  super().get_queryset()
        return queryset.filter(projeto__ativo=True)


class ClienteInativosView(ClienteView):

    template_name = "clientes-inativos.html"

    def get_queryset(self):
        queryset =  super().get_queryset()
        return queryset.filter(projeto__ativo=False)


class ClienteDetalhesView(DetailView):

    context_object_name = "cliente"
    template_name = "detalhes_clientes.html"
    model = Cliente


class ClimaView(ListView):

    context_object_name = "lista_climas"
    template_name = "clima.html"
    model = Clima


class ClimaDetalhesView(DetailView):

    context_object_name = "lista_climas"
    template_name = "detalhes_comunicados.html"
    model = Clima


class ColaboradoresView(ListView):

    context_object_name = "colaboradores"
    template_name = "colaboradores.html"
    model = Colaborador


class ColaboradoresDetalhesView(DetailView):

    context_object_name = "colaborador"
    template_name = "detalhes_colabs.html"
    model = Colaborador


class ContatoView(CreateView):

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


class CursoView(ListView):

    context_object_name = "curso"
    template_name = "cursos.html"
    model = Curso


class CursoDetalhesView(DetailView):

    context_object_name = "cursos"
    template_name = "detalhes_cursos.html"
    model = Curso


class FeedbackView(ListView):

    context_object_name = "feedback"
    template_name = "feedbacks.html"
    model = Feedback


class FeedbackDetalhesView(DetailView):

    context_object_name = "feedback"
    template_name = "detalhes_feedback.html"
    model = Feedback


class FerramentaView(ListView):

    context_object_name = "ferramentas"
    template_name = "ferramentas.html"
    model = Ferramenta


class FolguinhaView(ListView):

    context_object_name = "folguinha"
    template_name = "folgas.html"
    model = Folguinha


class FornecedoresView(ListView):

    context_object_name = "fornecedores"
    template_name = "fornecedores.html"
    model = Fornecedores

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["atividades"] = Atividadecomercial.objects.all()
        return context


class FornecedoresDetalhesView(DetailView):

    context_object_name = "fornecedores"
    template_name = "detalhes_fornecedores.html"
    model = Fornecedores


class HierarquiaView(ListView):

    context_object_name = "hierarquia"
    template_name = "hierarquias.html"
    model = Hierarquia


class InscricaoView(ListView):

    context_object_name = "inscricao"
    template_name = "inscricoes.html"
    model = Inscricao


class JuridicoView(ListView):

    context_object_name = "juridico"
    template_name = "juridicos.html"
    model = Juridico


class MomentoImportanteView(ListView):

    context_object_name = "MomentoImportante"
    template_name = "momentos.html"
    model = MomentoImportante


class NewsletterView(ListView):

    context_object_name = "newsletter"
    template_name = "newsletters.html"
    model = Newsletter


class NewsletterTotalView(ListView):

    context_object_name = "newslettertotal"
    model = NewsletterTotal


class PalestraView(ListView):

    context_object_name = "palestras"
    template_name = "palestras.html"
    model = Palestra


class PremiacaoView(ListView):

    context_object_name = "premiacoes"
    template_name = "premiacoes.html"
    model = Premiacao


class ProjetoView(ListView):

    context_object_name = "projetos"
    extra_context = {"form_contato": ContatoForm()}
    template_name = "projetos.html"
    model = Projeto


class ProjetoDetalhesView(DetailView):

    context_object_name = "projeto"
    template_name = "detalhes_projetos.html"
    model = Projeto


class PromocaoView(ListView):

    context_object_name = "promocao"
    template_name = "promocoes.html"
    model = Promocao


class PropostaView(ListView):

    context_object_name = "proposta"
    template_name = "propostas.html"
    model = Proposta


class PropostaDetalhesView(DetailView):

    context_object_name = "proposta"
    template_name = "detalhes_propostas.html"
    model = Proposta


class ResultadoCanalView(ListView):

    context_object_name = "resultadocanal"
    model = ResultadoCanal


class TipoProjetoView(ListView):

    context_object_name = "tipoprojeto"
    template_name = "tipo_projeto.html"
    model = TipoProjeto


class WorkshopView(ListView):

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
            "texto": "O Tuli acha que o Xis Porrada Será comprado pelo Raupps Lanches."
        }
        numero_dias_total = (data_fim - data_inicio).days
        numero_que_ja_passou_de_dias = (data_fim - datetime.now().date()).days
        context["progress_value"] = (numero_dias_total - numero_que_ja_passou_de_dias) / numero_dias_total * 100
        return context


class LoginShootView(LoginView):

    template_name = "login.html"


class LogoutShootView(LogoutView):

    next_page = reverse_lazy("juridicos")
