from django.views.generic import ListView
from rh.models import Colaborador, Fornecedores, Cliente, Projeto


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
    
    context_object_name = "projeto"
    template_name = "projetos.html"
    model = Projeto
