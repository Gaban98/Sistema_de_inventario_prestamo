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

class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['disponible']
        labels = {
            'disponible': 'Disponibilidad del elemento',
        }
        widgets = {
            'disponible': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la disponibilidad del elemento',
                    'id': 'disponible'
                }
            )
        }

class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = ['nombre', 'descripcion', 'estado', 'disponibilidad', 'sede', 'categoria']
        labels = {
            'nombre': 'Nombre del elemento',
            'descripcion': 'Descripción del elemento',
            'estado': 'Estado del elemento',
            'disponibilidad': 'Disponibilidad del elemento',
            'sede': 'Sede del elemento',
            'categoria': 'Categoría del elemento',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del elemento',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripción del elemento',
                    'id': 'descripcion'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el estado del elemento',
                    'id': 'estado'
                }
            ),
            'disponibilidad': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la disponibilidad del elemento',
                    'id': 'disponibilidad'
                }
            ),
            'sede': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la sede del elemento',
                    'id': 'sede'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la categoría del elemento',
                    'id': 'categoria'
                }
            ),
        }