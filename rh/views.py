from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from rh.models import (Cliente, Colaborador, Contato, Fornecedores, Projeto,
                       Proposta, TipoProjeto)


class IndexView(TemplateView):

    template_name = "index.html"

class ColaboradoresView(ListView):

    context_object_name = "colaboradores"
    template_name = "colaboradores.html"
    model = Colaborador

class FornecedoresView(ListView):

    context_object_name = "fornecedores"
    template_name = "fornecedores.html"
    model = Fornecedores

class ClienteView(ListView):

    context_object_name = "cliente"
    template_name = "clientes.html"
    model = Cliente

class ClienteDetalhesView(DetailView):

    context_object_name = "cliente"
    template_name = "detalhes_clientes.html"
    model = Cliente

class ProjetoView(ListView):

    context_object_name = "projetos"
    template_name = "projetos.html"
    model = Projeto

class ProjetoDetalhesView(DetailView):

    context_object_name = "projeto"
    template_name = "detalhes_projetos.html"
    model = Projeto

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

class ContatoView(CreateView):

    model = Contato
    fields = ["nome", "email", "mensagem"]
    template_name = "contato.html"
    success_url = reverse_lazy("lista_projeto")

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