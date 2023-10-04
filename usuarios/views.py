from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import JsonResponse
from .models import *
from .form import *
from inventario.views import *
from django.utils import timezone
from django.utils import timezone
from django.core import serializers



# Vista princpal
import datetime
import requests
from django.shortcuts import render

def index_view(request):
    # Obtener la hora actual
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Obtener la temperatura y descripción del clima en Ibagué
    api_key = "bc2638f8e4a4db5a407207c4a9beaef7"
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Ibague,CO&units=metric&appid={api_key}"
    
    response = requests.get(url)
    data = response.json()
    
    current_temperature = data['main']['temp']
    description = data['weather'][0]['description']

    # Pasar las variables al contexto
    context = {
        'current_date': current_date, # 'current_date' es el nombre de la variable que se usará en el template 'index.html
        'current_time': current_time,
        'current_temperature': current_temperature,
        'description': description,
    }
    
    return render(request, 'index.html', context)

# Vista para listar los usuarios
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuarios.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        return Usuario.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_usuario'] = UsuarioForm()  # Agregar el formulario al contexto
        return context

    def post(self, request, *args, **kwargs):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:usuario-list')
        else:
            context = self.get_context_data()
            context['form_usuario'] = form
            return self.render_to_response(context)


# Vista para editar un usuario existente
class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuarios/editar_usuarios.html'
    fields = ['cedula', 'nombres', 'apellidos', 'correo', 'celular']
    success_url = reverse_lazy('usuarios:usuario-list')

# Vista para eliminar un usuario
class UsuarioDeleteView(DeleteView):
    model = Usuario

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('usuarios:usuario-list')
    
###############################3 LOGICA DEL PRESTAMO ##########################################

def listarcrear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)  # No guardamos el préstamo todavía
            
            # Validación adicional de fecha
            if prestamo.fecha_prestamo < timezone.localtime().date():
                return render(request, 'usuarios/prestamo.html', {
                    'form': form,
                    'prestamos': Prestamo.objects.all(),
                    'error_message': "La fecha de préstamo no puede ser en el pasado."
                })
            
            if (prestamo.fecha_prestamo - timezone.localtime().date()).days > 380:
                return render(request, 'usuarios/prestamo.html', {
                    'form': form,
                    'prestamos': Prestamo.objects.all(),
                    'error_message': "La duración máxima del préstamo es de 380 días."
                })

            prestamo.save()

            # Obtenemos el elemento asociado al préstamo
            elemento = Elemento.objects.get(id=prestamo.elemento.id)

            # Cambiamos el estado del elemento a 'prestado'
            elemento.disponibilidad = 'Prestado'

            # Guardamos el elemento con su nuevo estado
            elemento.save()

            return redirect('usuarios:prestamo')  # Redirige a la misma vista para mostrar la lista actualizada
    else:
        form = PrestamoForm()
    
    prestamos = Prestamo.objects.filter(devuelto=False)  # Obtén todos los préstamos existentes
    
    return render(request, 'usuarios/prestamo.html', {'form': form, 'prestamos': prestamos})

def historial_prestamos(request):
    prestamos = Prestamo.objects.filter(devuelto=True)
    return render(request, 'usuarios/historial_prestamo.html', {'prestamos': prestamos})



def devolver_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)

    # Aquí actualizamos el estado del elemento a 'disponible'
    elemento = Elemento.objects.get(id=prestamo.elemento.id)
    elemento.disponibilidad = 'Disponible'
    elemento.save()

    # Aquí marcamos el préstamo como devuelto
    prestamo.fecha_devolucion = timezone.now()
    prestamo.devuelto = True
    prestamo.save()

    return redirect('usuarios:prestamo')
    
