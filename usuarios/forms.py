from django import forms
from .models import *

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'cedula', 'telefono', 'direccion', 'email', 'password', 'rol']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cedula': 'Cedula',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'email': 'Email',
            'password': 'Password',
            'rol': 'Rol',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido',
                    'id': 'apellido'
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cedula',
                    'id': 'cedula'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el telefono',
                    'id': 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la direccion',
                    'id': 'direccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el email',
                    'id': 'email'
                }
            ),
        }