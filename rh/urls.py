from django.conf.urls import include, url
from django.urls import path

from rh.views import (BibliotecaView, ClienteDetalhesView, ClienteView,
                      ClimaDetalhesView, ClimaView, ColaboradoresDetalhesView,
                      ColaboradoresView, ContatoView, CursoDetalhesView,
                      CursoView, FeedbackView, FolguinhaView, FornecedoresView,
                      HierarquiaView, IndexView, MomentoImportanteView,
                      ProjetoDetalhesView, ProjetoView, PromocaoView,
                      PropostaDetalhesView, PropostaView, TipoProjetoView)

urlpatterns = [
    path("biblioteca/", BibliotecaView.as_view(), name="biblioteca"),
    path("clientes/", ClienteView.as_view(), name="lista_cliente"),
    path("clientes/<int:pk>/", ClienteDetalhesView.as_view(), name="detalhes_cliente"),
    path("clima/", ClimaView.as_view(), name="lista_climas"),
    path("clima/<int:pk>/", ClimaDetalhesView.as_view(), name="clima"),
    path("colaboradores/", ColaboradoresView.as_view(), name="lista_colaboradores"),
    path("colaboradores/<int:pk>/", ColaboradoresDetalhesView.as_view(), name="detalhes_colaborador"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("curso/", CursoView.as_view(), name="curso"),
    path("curso/<int:pk>/", CursoDetalhesView.as_view(), name="lista_curso"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("folguinha/", FolguinhaView.as_view(), name="folguinha"),
    path("fornecedores/", FornecedoresView.as_view(), name="lista_fornecedores"),
    path("hierarquia/", HierarquiaView.as_view(), name="hierarquia"),
    path("", IndexView.as_view(), name="index"),
    path("momentos/", MomentoImportanteView.as_view(), name="MomentoImportante"),
    path("projetos/", ProjetoView.as_view(), name="lista_projeto"),
    path("projetos/<int:pk>/", ProjetoDetalhesView.as_view(), name="detalhes_projeto"),
    path("promocao/", PromocaoView.as_view(), name="promocao"),
    path("propostas/", PropostaView.as_view(), name="lista_proposta"),
    path("propostas/<int:pk>/", PropostaDetalhesView.as_view(), name="detalhes_proposta"),
    path("tipo_projeto/", TipoProjetoView.as_view(), name="lista_TipoProjeto"),
    
]
