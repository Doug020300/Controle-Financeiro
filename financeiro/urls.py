from django.contrib import admin
from django.urls import path
from contas import views  # Importa as views do nosso app 'contas'

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel de administração
    path('', views.extrato, name='extrato'),  # Rota para a página inicial
]