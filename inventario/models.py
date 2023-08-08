from django.db import models
from usuarios.models import Usuario

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos relevantes para la sede

    def __str__(self):
        return self.nombre

# Definimos las opciones para el campo "estado"
OPCIONES_ESTADO = (
    ('buen_estado', 'En buen estado'),
    ('mal_estado', 'En mal estado'),
)

class Elemento(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='buen_estado')
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre
