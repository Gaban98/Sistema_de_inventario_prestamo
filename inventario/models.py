from django.db import models

OPCIONES_ESTADO = [
    ('buen_estado', 'Buen estado'),
    ('mal_estado', 'Mal estado'),
    ('en_reparacion', 'En reparación'),
]

OPCIONES_DISPONIBILIDAD = [
    ('disponible', 'Disponible'),
    ('prestado', 'Prestado'),
    ('dañado', 'Dañado'),
    ('reparacion', 'Reparación'),  # Cambiado a 'reparacion' para coincidir con las opciones del modelo.
]

# vamos a trabajar los estados del elemento desde la table prestamos

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    jefe_directo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Elemento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    estado = models.CharField(max_length=15, choices=OPCIONES_ESTADO, default='Buen estado')
    disponibilidad = models.CharField(max_length=20, choices=OPCIONES_DISPONIBILIDAD, default='Disponible')
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# aca unicamente debe crear disponible y en buen estado por defecto para que despues el pueda editarlo desde lo perosonal y asi