
from django.db import models

class Usuario(models.Model):
    cedula = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    celular = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

