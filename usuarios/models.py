from django.db import models
from inventario.models import Sede, Elemento
from django.utils import timezone

class Usuario(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    celular = models.CharField(max_length=15)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Agregamos validación de fecha al guardar el préstamo
        if self.fecha_prestamo < timezone.now().date():
            raise ValueError("La fecha de préstamo no puede ser en el pasado.")
        
        if (self.fecha_prestamo - timezone.now().date()).days > 380:
            raise ValueError("La duración máxima del préstamo es de 380 días.")
        
        super(Prestamo, self).save(*args, **kwargs)
