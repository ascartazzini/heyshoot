from django.views.generic import ListView
from rh.models import Colaborador


class ColaboradoresView(ListView):

    context_object_name = "colaboradores"
    template_name = "colaboradores.html"
    model = Colaborador


class ColaboradoresNegrosView(ColaboradoresView):

    queryset = Colaborador.objects.filter(eh_negra=True)
