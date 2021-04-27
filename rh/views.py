from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib import messages

from rh.models import (Cliente, Colaborador, Contato, Fornecedores, Projeto,
                       Proposta, TipoProjeto)


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

class TipoProjetoView(ListView):

    context_object_name = "TipoProjeto"
    template_name = "tipo_projeto.html"
    model = TipoProjeto


class ContatoView(CreateView):

    model = Contato
    fields = ["nome", "email", "mensagem"]
    template_name = "contato.html"
    success_url = reverse_lazy("lista_projeto")

    def form_valid(self, form):
        messages.success(self.request, "Seu formulário foi enviado. Aguardo o Tuli responder.")
        return super().form_valid(form)
