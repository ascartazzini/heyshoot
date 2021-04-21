from rh.views import ColaboradoresView, FornecedoresView, ClienteView, ProjetoView, PropostaView, TipoProjetoView
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path("colaboradores/", ColaboradoresView.as_view(), name="lista_colaboradores"),
    path("fornecedores/", FornecedoresView.as_view(), name="lista_fornecedores"),
    path("clientes/", ClienteView.as_view(), name="lista_cliente"),
    path("projetos/", ProjetoView.as_view(), name="lista_projeto"),
    path("propostas/", PropostaView.as_view(), name="lista_proposta"),
    path("tipo_projeto/", TipoProjetoView.as_view(), name="lista_TipoProjeto"),
]
