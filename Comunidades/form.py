from django import forms

from Comunidades.models import Comunidades


class ComunidadesForm(forms.ModelForm):
    class Meta:
        model = Comunidades
        exclude = []
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Fecha'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'fuente': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enlace'}),
            'cobertura': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': 'Cobertura'}),
            'tip_comunidad': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': 'Tipología'}),
            'tematica': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Temática'}),
            'afiliacion': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': 'Afiliación'}),
            'coordinador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coordinador'}),
        }
        labels = {
            'fecha': 'Fecha',
            'categoria': 'Categoría',
            'nombre': 'Nombre',
            'fuente': 'Enlace',
            'cobertura': 'Cobertura',
            'tip_comunidad': 'Tipología_Comunidad',
            'tematica': 'Temática',
            'afiliacion': 'Afiliación',
            'coordinador': 'Coordinador',
        }
