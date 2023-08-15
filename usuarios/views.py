from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .models import Usuario
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
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'

# Vista para crear un nuevo usuario
class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuarios/usuario_form.html'
    fields = ['cedula', 'nombres', 'apellidos', 'correo', 'celular']
    success_url = reverse_lazy('usuario-list')

# Vista para editar un usuario existente
class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuarios/usuario_form.html'
    fields = ['cedula', 'nombres', 'apellidos', 'correo', 'celular']
    success_url = reverse_lazy('usuario-list')

# Vista para eliminar un usuario
class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario-list')


