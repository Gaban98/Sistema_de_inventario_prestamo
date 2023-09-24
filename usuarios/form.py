from django import forms
from .models import *



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cedula', 'nombres', 'apellidos', 'correo', 'celular', 'sede']
        labels = {
            'cedula': 'Cedula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'correo': 'Correo',
            'celular': 'Celular',
            'sede': 'Sede',
        }
        widgets = {
            'cedula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cedula',
                    'id': 'cedula'
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los nombres',
                    'id': 'nombres'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los apellidos',
                    'id': 'apellidos'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo',
                    'id': 'correo'
                }
            ),
            'celular': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el celular',
                    'id': 'celular'
                }
            ),
            'sede': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'sede'
                }
            ),
        }

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['usuario', 'elemento', 'fecha_prestamo', 'fecha_devolucion']
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['elemento'].queryset = Elemento.objects.filter(disponibilidad='Disponible')
