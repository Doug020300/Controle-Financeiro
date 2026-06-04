from django.contrib import admin
from .models import Transacao

# Registra a tabela no painel de controle administrativo
admin.site.register(Transacao)