from django import forms
from .models import crm

class crm_form(forms.ModelForm):
    class Meta:
        model = crm
        fields = '__all__' # inclui todos os campos do modelo crm