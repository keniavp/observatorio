from django import forms

from Eventos.models import EventosConv


class EventosForm(forms.ModelForm):
    class Meta:
        model = EventosConv
        exclude = []
        widgets = {
            'nombre': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'imagen': forms.TextInput(attrs={'type': 'file', 'class': 'form-control', 'placeholder': 'Imagen'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
            'entidad_responsable': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Entidad Responsable'}),
            'enlace': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enlace'}),
            'fuente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fuente'}),
            'descriptores': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descriptor'}),
        }
        labels = {
            'nombre': 'Nombre',
            'imagen': 'Imagen',
            'categoria': 'Categoría',
            'entidad_responsable': 'Entidad Responsable',
            'enlace': 'Enlace',
            'fuente': 'Fuente',
            'descriptores': 'Descriptor',
        }