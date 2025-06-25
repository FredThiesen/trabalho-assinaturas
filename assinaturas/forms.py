from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Assinatura
from clientes.models import Cliente

class AssinaturaForm(forms.ModelForm):
    clientes = forms.ModelMultipleChoiceField(
        queryset=Cliente.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn btn-primary'))
        self.helper.add_input(Submit('cancel', 'Cancelar', css_class='btn btn-secondary', formnovalidate='formnovalidate', onclick="window.location.href='/assinaturas/';return false;"))

    class Meta:
        model = Assinatura
        fields = ['nome', 'mensalidade', 'clientes']
