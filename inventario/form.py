from django import forms
from .models import *

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre de la categoría',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de la categoría',
                    'id': 'nombre'
                }
            )
        }

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['nombre', 'direccion', 'telefono', 'jefe_directo']
        labels = {
            'nombre': 'Nombre de la sede',
            'direccion': 'Dirección de la sede',
            'telefono': 'Teléfono de la sede',
            'jefe_directo': 'Jefe directo de la sede',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de la sede',
                    'id': 'nombre'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección de la sede',
                    'id': 'direccion'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el teléfono de la sede',
                    'id': 'telefono'
                }
            ),
            'jefe_directo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el jefe directo de la sede',
                    'id': 'jefe_directo'
                }
            ),
        }

class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = ['nombre', 'descripcion', 'sede', 'categoria']
        labels = {
            'nombre': 'Nombre del elemento',
            'descripcion': 'Descripción del elemento',
            'sede': 'Sede del elemento',
            'categoria': 'Categoría del elemento',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del elemento', 'id': 'nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción del elemento', 'id': 'descripcion'}),
            'sede': forms.Select(attrs={'class': 'form-control', 'id': 'sede'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'id': 'categoria'}),
            'estado': forms.HiddenInput(),  # Oculta el campo estado
            'disponibilidad': forms.HiddenInput(),  # Oculta el campo disponibilidad
        }
        


class FiltroElementosForm(forms.Form):
    disponibilidad = forms.ChoiceField(choices=OPCIONES_DISPONIBILIDAD, required=False, label="Filtrar por Disponibilidad")