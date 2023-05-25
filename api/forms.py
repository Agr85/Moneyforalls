from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'email', 'sexo', 'pais', 'estoy_de_acuerdo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['required'] = True
        self.fields['email'].widget.attrs['required'] = True
        self.fields['sexo'].widget.attrs['required'] = True
        self.fields['pais'].widget.attrs['required'] = True
        self.fields['estoy_de_acuerdo'].widget.attrs['required'] = True
