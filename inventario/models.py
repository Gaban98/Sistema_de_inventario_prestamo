from django.db import models
from usuarios.models import Usuario


OPCIONES_ESTADO = [
    ('buen_estado', 'Buen estado'),
    ('mal_estado', 'Mal estado'),
    ('en_reparacion', 'En reparación'),
]

class Elemento(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Buen estado')
    disponible = models.BooleanField(default=True)  # Indica si está disponible

    def __str__(self):
        return self.nombre


from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_celular = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
