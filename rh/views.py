from django.views.generic import DetailView, ListView

from rh.models import (Cliente, Colaborador, Fornecedores, Projeto, Proposta,
                       TipoProjeto)


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
