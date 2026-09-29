from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("servicos/novo/", views.novo_servico, name="novo_servico"),
    path("servicos/detalhes/", views.detalhe_servico, name="detalhe_servico"),
]
