from django.contrib.auth.models import AbstractUser
from django.db import models

class Empresa(models.Model):  # Nome de classe em maiúscula (boas práticas)
    nome_empresa = models.CharField(max_length=45, unique=True)
    cnpj_cpf = models.CharField(max_length=18, unique=True)  # Aceita CPF ou CNPJ
    cep = models.CharField(max_length=9)  # Formato: "00000-000"

    def __str__(self):
        return self.nome_empresa

class CustomUser(AbstractUser):
    empresa = models.ForeignKey(
        Empresa,  # Agora a classe está definida antes
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="usuarios"
    )

    def __str__(self):
        return f"{self.username} ({self.empresa.nome_empresa if self.empresa else 'Sem empresa'})"
