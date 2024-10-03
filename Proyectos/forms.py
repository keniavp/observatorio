from django import forms

from Proyectos.models import Proyectos


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        exclude = []
        widgets = {
            'ambito': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': 'Nombre'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipología'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aprobado'}),
            'entidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organismo'}),
            'pais': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': 'Año'}),
            'provincia': forms.Select(attrs={'class': 'form-control custom-select'}),
            'municipio': forms.Select(attrs={'class': 'form-control custom-select'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto'}),
            'fuente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto'}),
            'descriptor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto'}),
        }
        labels = {
            'ambito': 'Ámbito',
            'nombre': 'Nombre',
            'categoria': 'Categoría',
            'imagen': 'Imagen',
            'entidad': 'Entidad',
            'pais': 'País',
            'provincia': 'Provincia',
            "municipio": "Municipio",
            "region": "Región",
            "fuente": "Fuente",
            "year": "Año",
            "url": "Enlace",
            "descriptor": "Descriptor",
        }
