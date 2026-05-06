from django import forms
from .models import Categoria, Prenda


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class PrendaForm(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = '__all__'