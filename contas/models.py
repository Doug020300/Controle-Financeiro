from django.db import models

class Transacao(models.Model):
    # Opções para o tipo de transação (Entrada ou Saída)
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SAIDA', 'Saída'),
    ]

    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    categoria = models.CharField(max_length=50)
    data = models.DateField()

    # Define como a transação será exibida na tela de administração (pelo nome/descrição)
    def __str__(self):
        return self.descricao