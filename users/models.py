from django.contrib.auth.models import AbstractUser
from django.db import models
from crm.models import empresa  # Importando o modelo Empresa

class CustomUser(AbstractUser):
    empresa = models.ForeignKey(
        empresa, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="usuarios"
    )

    def __str__(self):
        return f"{self.username} ({self.empresa.nome_empresa if self.empresa else 'Sem empresa'})"
