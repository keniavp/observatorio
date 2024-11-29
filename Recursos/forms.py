from django import forms

from Recursos.models import RecursosA


class RecursosForm(forms.ModelForm):
    class Meta:
        model = RecursosA
        exclude = []
        widgets = {
            'tipo_r': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': 'Seleccionar Tipo de Recurso'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar Nombre'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar Categoría'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'entidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Insertar Entidad'}),
            'pais': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': 'Seleccionar País'}),
            'provincia': forms.Select(attrs={'class': 'form-control custom-select'}),
            'municipio': forms.Select(attrs={'class': 'form-control custom-select'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar Región'}),
            'fuente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Insertar Fuente'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar año'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar Enlace'}),
            'descriptor': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insertar Descripción'}),
        }
        labels = {
            'ambito': 'Ámbito',
            'nombre': 'Nombre',
            'categoria': 'Categoría',
            'imagen': 'Imagen',
            'entidad': 'Entidad Responsable',
            'pais': 'País',
            'provincia': 'Provincia',
            "municipio": "Municipio",
            "region": "Región",
            "fuente": "Fuente",
            "year": "Año",
            "url": "Enlace",
            "descriptor": "Descripción",
        }
