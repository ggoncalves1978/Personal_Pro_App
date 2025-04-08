from django import forms
from .models import Empresa, CustomUser

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["nome_empresa", "cnpj_cpf", "cep"]

class CustomUserForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["first_name", "username", "email", "senha"]
