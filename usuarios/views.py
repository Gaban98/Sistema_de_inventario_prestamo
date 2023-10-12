from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import *
from .models import *
from .form import *
from inventario.views import *
from django.utils import timezone


import datetime
import pytz
def index_view(request):
    return render(request, 'index.html')

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
        
    def get_queryset(self):
        sede_id = self.kwargs.get('sede_id')
        if sede_id:
            return Usuario.objects.filter(sede=sede_id)
        else:
            return Usuario.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_usuario'] = UsuarioForm()  # Agregar el formulario al contexto
        context['sedes'] = Sede.objects.all()  # Agregar todas las sedes al contexto
        return context


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
            prestamo = form.save(commit=False)

            # Cambiamos el estado del elemento a 'prestado' y guardamos el elemento
            prestamo.elemento.disponibilidad = 'Prestado'
            prestamo.elemento.save()

            prestamo.save()

            # Actualizamos la lista de elementos disponibles en el formulario
            form.fields['elemento'].queryset = Elemento.objects.filter(disponibilidad='Disponible')

            return redirect('usuarios:prestamo')  # Redirige a la misma vista para mostrar la lista actualizada
    else:
        form = PrestamoForm()
    
    prestamos = Prestamo.objects.filter(devuelto=False)
    
    return render(request, 'usuarios/prestamo.html', {'form': form, 'prestamos': prestamos})


def historial_prestamos(request):
    prestamos = Prestamo.objects.filter(devuelto=1)
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

def elementos_por_categoria(request, categoria_id):
    elementos = Elemento.objects.filter(categoria_id=categoria_id, disponibilidad='Disponible')
    elementos_json = [{'id': elemento.id, 'nombre': elemento.nombre} for elemento in elementos]
    return JsonResponse(elementos_json, safe=False)


