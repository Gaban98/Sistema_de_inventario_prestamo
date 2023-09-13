from django.db import models
from inventario.models import Sede, Elemento


OPCIONES_PRESTAMO = (
    ('Prestado', 'Prestado'),
    ('Disponible', 'Disponible'),
    ('Dañado', 'Dañado'),
    ('En reparación', 'En reparación'),
    ('En mantenimiento', 'En mantenimiento'),
    ('En baja', 'En baja'),
)
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
    estado = models.CharField(max_length=20, choices=OPCIONES_PRESTAMO, default='Disponible')

# cuando yo vaya a prestar un elemento, debo cambiar el estado del elemento a prestado
# no puedo prestar nada dañado, nada en mal estado, debe estar disponible y en buen estado# ademas se deben 
# mofidicadiones en el modelo de prestamo, para que cuando se devuelva el elemento, se cambie el estado del elemento


#aca debo hacer la table de opciones de disponbilidad y estado, para que cuando se preste un elemento, se cambie el estado del elemento