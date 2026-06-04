from django.shortcuts import render, redirect  # Adicionamos o 'redirect'
from .models import Transacao

def extrato(request):
    # 1. Se for uma requisição POST, o usuário está enviando o formulário
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        tipo = request.POST.get('tipo')
        categoria = request.POST.get('categoria')
        data = request.POST.get('data')

        # Cria o registro da nova transação no banco de dados SQLite
        Transacao.objects.create(
            descricao=descricao,
            valor=valor,
            tipo=tipo,
            categoria=categoria,
            data=data
        )
        # Redireciona de volta para a página inicial (limpa o formulário e atualiza a tela)
        return redirect('extrato')

    # 2. Se for uma requisição GET (acesso comum), apenas exibe os dados e faz as somas
    transacoes = Transacao.objects.all()
    total_entradas = 0
    total_saidas = 0

    for transacao in transacoes:
        if transacao.tipo == 'ENTRADA':
            total_entradas += transacao.valor
        else:
            total_saidas += transacao.valor

    saldo = total_entradas - total_saidas

    contexto = {
        'transacoes': transacoes,
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
        'saldo': saldo
    }
    return render(request, 'contas/extrato.html', contexto)