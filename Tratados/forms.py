from django import forms

from Tratados.models import TratadosI


class TratadoForm(forms.ModelForm):
    class Meta:
        model = TratadosI
        exclude = []
        widgets = {
            'nombre': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'tipologia': forms.Select(attrs={'class': 'form-control custom-select', 'placeholder': 'Tipología'}),
            'categoria': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'aprobado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aprobado'}),
            'organismo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organismo'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Año'}),
            'pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'concepto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Concepto'}),
        }
        labels = {
            'tipologia': 'Tipología',
            'categoria': 'Categoría',
            'aprobado': 'Aprobado',
            'organismo': 'Organismo',
            'year': 'Año',
            'pdf': 'PDF',
            'imagen': 'Imagen',
            "concepto": "Concepto"
        }
