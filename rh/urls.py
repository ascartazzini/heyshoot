from rh.views import ColaboradoresView, FornecedoresView
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path("colaboradores/", ColaboradoresView.as_view(), name="lista_colaboradores"),
    path("fornecedores/", ColaboradoresView.as_view(), name="lista_fornecedores"),
]
