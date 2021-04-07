from rh.views import ColaboradoresView, ColaboradoresNegrosView
from django.conf.urls import include, url
from django.urls import path


urlpatterns = [
    path("colaboradores/", ColaboradoresView.as_view(), name="lista_colaboradores"),
    path("colaboradores/negros/", ColaboradoresNegrosView.as_view(), name="lista_colaboradores_negros"),
]
