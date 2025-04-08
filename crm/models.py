from django.db import models

class crm(models.Model):
    nome = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    pais = models.CharField(max_length=45)
    data_do_contato = models.DateField()
    dia_da_semana = models.CharField(max_length=45)
    canal = models.CharField(max_length=45)
    data_de_fechamento = models.DateField()
    follow_up = models.CharField(max_length=3)
    chegou_na_oferta = models.CharField(max_length=45)
    plano_escolhido = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.telefone}"

