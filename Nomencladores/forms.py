from django import forms

from Nomencladores.models import Afiliacion, Clasificacion, Provincia,Municipio, Region,Tematica,Tipologia,Pais,Cobertura,ComunidadesAcademicas

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        exclude = []
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar país', 'max_length':'15'}),
            'siglas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            'bandera': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'País',
            'siglas': 'Siglas',
            'bandera':'Bandera'           
        }

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        exclude = []
        widgets = {
            'provincia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar provincia', 'max_length':'15'}),
            'siglas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            
        }
        labels = {
            'provincia': 'Provincia',
            'siglas': 'Siglas',            
        }
        
class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        exclude = []
        widgets = {
            'municipio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar municipio'}),
            'siglas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            'provincia': forms.Select(attrs={'class': 'form-control custom-select'}),
        }
        labels = {
            'municipio': 'Municipio',
            'siglas': 'Siglas',            
            'provincia': 'Provincia',            
        }
        
class TipologiaForm(forms.ModelForm):
    class Meta:
        model = Tipologia
        exclude = []
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar municipio'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            
        }
        labels = {
            'tipologia': 'Tipologia',
            'sigla': 'Siglas',            
                       
        }
        
class CoberturaForm(forms.ModelForm):
    class Meta:
        model = Cobertura
        exclude = []
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar cobertura'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            
        }
        labels = {
            'nombre': 'Cobertura',
            'sigla': 'Siglas',            
                       
        }
        
class TematicaForm(forms.ModelForm):
    class Meta:
        model = Tematica
        exclude = []
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar temática'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            
        }
    labels = {
        'nombre': 'Temática',
        'sigla': 'Siglas',            
                    
    }

class ComunidadaForm(forms.ModelForm):
    class Meta:
        model = ComunidadesAcademicas
        exclude = []
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar comunidad'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            
        }
    labels = {
        'nombre': 'Comunidad',
        'sigla': 'Siglas',            
                    
    }
    
class AfiliacionForm(forms.ModelForm):
    class Meta:
        model = Afiliacion
        exclude = []
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar afiliación'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            
        }
    labels = {
        'nombre': 'Afiliación',
        'sigla': 'Siglas',            
                    
    }
    
class ClasificacionForm(forms.ModelForm):
    class Meta:
        model = Clasificacion
        exclude = []
        widgets = {
            'clasif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar clasificación'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            
        }
    labels = {
        'clasif': 'Clasificación',
        'sigla': 'Siglas',            
                    
    }
    
class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        exclude = []
        widgets = {
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar región'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar siglas'}),
            
        }
    labels = {
        'region': 'Región',
        'sigla': 'Siglas',            
                    
    }

