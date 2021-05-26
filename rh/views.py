from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from rh.forms import ContatoForm
from rh.models import (Atividadecomercial, Biblioteca, Cliente, Clima,
                       Colaborador, Contato, Curso, Feedback, Folguinha,
                       Fornecedores, Hierarquia, MomentoImportante, PapoCabeca,
                       Projeto, Promocao, Proposta, TipoProjeto)


class IndexView(TemplateView):

    template_name = "index.html"


class BibliotecaView(ListView):

    context_object_name = "biblioteca"
    template_name = "biblioteca.html"
    model = Biblioteca


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


class PapoCabecaView(ListView):
    
    context_object_name = "mesaredonda"
    template_name = "mesaredonda.html"
    model = PapoCabeca


class MomentoImportanteView(ListView):

    context_object_name = "MomentoImportante"
    template_name = "momentos.html"
    model = MomentoImportante


class HierarquiaView(ListView):

    context_object_name = "hierarquia"
    template_name = "hierarquias.html"
    model = Hierarquia


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


class TipoProjetoView(ListView):

    context_object_name = "tipoprojeto"
    template_name = "tipo_projeto.html"
    model = TipoProjeto
