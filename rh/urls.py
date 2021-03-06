from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.urls import path

from rh.views import (AtivismoDetalhesView, AtivismoView, BibliotecaView,
                      CanaisProprietariosView, CertificacaoView,
                      ClienteAtivosView, ClienteDetalhesView,
                      ClienteInativosView, ClienteView, ClimaDetalhesView,
                      ClimaView, ColaboradoresDetalhesView, ColaboradoresView,
                      ContatoView, CursoDetalhesView, CursoView,
                      FeedbackDetalhesView, FeedbackView, FerramentaView,
                      FinanceiroDetalhesView, FinanceiroTotalView,
                      FolguinhaView, FornecedoresDetalhesView,
                      FornecedoresView, HierarquiaView, IndexView,
                      InscricaoView, JuridicoView, LoginShootView,
                      LogoutShootView, MomentoImportanteView, NewsletterView,
                      PalestraView, PremiacaoView, ProjetoDetalhesView,
                      ProjetoView, PromocaoView, PropostaDetalhesView,
                      PropostaView, ResultadoCanalView, TipoProjetoView,
                      VisaoView, WorkshopView)

urlpatterns = [
    path("ativismo/", AtivismoView.as_view(), name="ativismo"),
    path("ativismo/<int:pk>/", AtivismoDetalhesView.as_view(), name="detalhes_ativismo"),
    path("biblioteca/", BibliotecaView.as_view(), name="biblioteca"),
    path("canais/", CanaisProprietariosView.as_view(), name ="canaisproprietarios"),
    path("certificacoes/", CertificacaoView.as_view(), name ="certificacoes"),
    path("clientes/", ClienteView.as_view(), name="lista_cliente"),
    path("clientes/ativos/", ClienteAtivosView.as_view(), name="lista_cliente_ativos"),
    path("clientes/inativos/", ClienteInativosView.as_view(), name="lista_cliente_inativos"),
    path("clientes/<int:pk>/", ClienteDetalhesView.as_view(), name="detalhes_cliente"),
    path("clima/", ClimaView.as_view(), name="lista_climas"),
    path("clima/<int:pk>/", ClimaDetalhesView.as_view(), name="clima"),
    path("colaboradores/", ColaboradoresView.as_view(), name="lista_colaboradores"),
    path("colaboradores/<int:pk>/", ColaboradoresDetalhesView.as_view(), name="detalhes_colaborador"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("curso/", CursoView.as_view(), name="curso"),
    path("curso/<int:pk>/", CursoDetalhesView.as_view(), name="lista_curso"),
    path("feedback/", FeedbackView.as_view(), name="feedback"),
    path("ferramentas/", FerramentaView.as_view(), name="ferramentas"),
    path("feedback/<int:pk>/", FeedbackDetalhesView.as_view(), name="detalhes_feedback"),
    path("financeiro/", FinanceiroTotalView.as_view(), name="contas"),
    path("financeiro/<int:pk>/", FinanceiroDetalhesView.as_view(), name="contas"),
    path("folguinha/", FolguinhaView.as_view(), name="folguinha"),
    path("fornecedores/", FornecedoresView.as_view(), name="lista_fornecedores"),
    path("fornecedores/<int:pk>/", FornecedoresDetalhesView.as_view(), name="detalhes_fornecedores"),
    path("hierarquia/", HierarquiaView.as_view(), name="hierarquia"),
    path("inscricao/", InscricaoView.as_view(), name = "inscricao"),
    path("", IndexView.as_view(), name="index"),
    path("juridicos/", JuridicoView.as_view(), name = "juridicos"),
    path("momentos/", MomentoImportanteView.as_view(), name="MomentoImportante"),
    path("newsletters/", NewsletterView.as_view(), name="newsletter"),
    path("palestra/", PalestraView.as_view(), name="palestras"),
    path("premiacao/", PremiacaoView.as_view(), name="premiacoes"),
    path("projetos/", ProjetoView.as_view(), name="lista_projeto"),
    path("projetos/<int:pk>/", ProjetoDetalhesView.as_view(), name="detalhes_projeto"),
    path("promocao/", PromocaoView.as_view(), name="promocao"),
    path("propostas/", PropostaView.as_view(), name="lista_proposta"),
    path("propostas/<int:pk>/", PropostaDetalhesView.as_view(), name="detalhes_proposta"),
    path("resultados/", ResultadoCanalView.as_view(), name="resultadoscanais"),
    path("tipo-projeto/", TipoProjetoView.as_view(), name="lista_TipoProjeto"),
    path("workshop/", WorkshopView.as_view(), name="workshop"),
    path("visao/", VisaoView.as_view(), name="visao"),
    path("login/", LoginShootView.as_view(), name="login"),
    path("logout/", LogoutShootView.as_view(), name="logout"),
]
