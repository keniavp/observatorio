from django import forms

from Ordenamiento.models import *


class OrdenamientoForm(forms.ModelForm):
    class Meta:
        model = OrdenamientoJ
        exclude = []
        widgets = {
            'nombre': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'tipologia': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Tipología'}),
            'categoria': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'aprobado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aprobado'}),
            'entidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entidad'}),
            'url': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enlace'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Año'}),
            'pdf': forms.FileInput(attrs={'class': 'form-control'}),
          
        }
        labels = {
            'nombre': 'Nombre',
            'tipologia': 'Tipología',
            'categoria': 'Categoría',
            'aprobado': 'Aprobado',
            'entidad': 'Entidad',
            'year': 'Año',
            'concepto': 'Concepto',
            "url": "Enlace",
            "pdf": "PDF",
        }
        
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        exclude = []
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'concepto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto'}),
        }
        labels = {
            'nombre': 'Nombre',
            'concepto': 'Concepto',            
        }