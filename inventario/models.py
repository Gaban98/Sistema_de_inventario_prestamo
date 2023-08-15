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

class Elemento(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Buen estado')
    disponible = models.BooleanField(default=True)  # Indica si está disponible

    def __str__(self):
        return self.nombre
