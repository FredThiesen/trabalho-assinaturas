from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Cliente

class ClienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            },
            format='%Y-%m-%d'
        ),
        input_formats=['%Y-%m-%d']
    )
    class Meta:
        model = Cliente
        fields = ['nome', 'data_nascimento', 'cpf', 'email']
