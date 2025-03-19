from django import forms
from .models import crm, empresa

class crm_form(forms.ModelForm):
    class Meta:
        model = crm
        fields = '__all__' # inclui todos os campos do modelo crm


class empresaForm(forms.ModelForm):
    class Meta:
        model = empresa
        fields = ["nome_empresa", "cnpj_cpf", "cep"]
        labels = {
            "nome_empresa": "Nome da Empresa",
            "cnpj_cpf": "CNPJ ou CPF",
            "cep": "CEP"
        }
        widgets = {
            "nome_empresa": forms.TextInput(attrs={"class": "form-control"}),
            "cnpj_cpf": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite CNPJ ou CPF"}),
            "cep": forms.TextInput(attrs={"class": "form-control", "placeholder": "00000-000"})
        }
