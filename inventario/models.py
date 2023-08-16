from django.db import models

OPCIONES_ESTADO = [
    ('buen_estado', 'Buen estado'),
    ('mal_estado', 'Mal estado'),
    ('en_reparacion', 'En reparación'),
]
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    jefe_directo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Disponibilidad(models.Model):
    OPCIONES_DISPONIBILIDAD = (
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('danado', 'Dañado'),
        ('reparación', 'Reparación'),
    )

    disponible = models.CharField(max_length=20, choices=OPCIONES_DISPONIBILIDAD)

    def __str__(self):
        return self.estado


class Elemento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Buen estado')
    disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
