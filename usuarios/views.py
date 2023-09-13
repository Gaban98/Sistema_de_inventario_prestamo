from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .form import *
import requests
import datetime


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
            form.save()
            return redirect('usuarios:prestamo')  # Redirige a la misma vista para mostrar la lista actualizada
    else:
        form = PrestamoForm()
    
    prestamos = Prestamo.objects.all()  # Obtén todos los préstamos existentes
    
    return render(request, 'usuarios/prestamo.html', {'form': form, 'prestamos': prestamos})

