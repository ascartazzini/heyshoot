from django.views.generic import ListView
from rh.models import Colaborador, Fornecedores


class ColaboradoresView(ListView):

    context_object_name = "colaboradores"
    template_name = "colaboradores.html"
    model = Colaborador

class FornecedoresView(ListView):
    
    context_object_name = "fornecedores"
    template_name = "fornecedores.html"
    model = Fornecedores
