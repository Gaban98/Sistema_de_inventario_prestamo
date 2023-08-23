from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .form import *

###################     Para AGREGAR    ######################

class CrearSede(CreateView):
    model = Sede
    fields = ['nombre', 'direccion', 'telefono', 'jefe_directo']
    template_name = 'nombre_del_template.html'
    success_url = '/donde_redirigir_despues_de_crear'

class CrearCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'nombre_del_template.html'
    success_url = '/donde_redirigir_despues_de_crear'

class CrearElemento(CreateView):
    model = Elemento
    fields = ['nombre', 'descripcion', 'estado', 'disponibilidad', 'sede', 'categoria']
    template_name = 'nombre_del_template.html'
    success_url = '/donde_redirigir_despues_de_crear'

###################     Para EDITAR     ######################

class ActualizarSede(UpdateView):
    model = Sede
    fields = ['nombre', 'direccion', 'telefono', 'jefe_directo']
    template_name = 'nombre_del_template.html'
    success_url = '/donde_redirigir_despues_de_editar'

class ActualizarCategoria(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'nombre_del_template.html'
    success_url = '/donde_redirigir_despues_de_editar'

class ActualizarElemento(UpdateView):
    model = Elemento
    fields = ['nombre', 'descripcion', 'estado', 'disponibilidad', 'sede', 'categoria']
    template_name = 'nombre_del_template.html'
    success_url = '/donde_redirigir_despues_de_editar'

###################     Para ELIMINAR   ######################

class EliminarSede(DeleteView):
    model = Sede
    template_name = 'nombre_del_template.html'
    success_url = '/donde_redirigir_despues_de_eliminar'

class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'nombre_del_template.html'
    success_url = '/donde_redirigir_despues_de_eliminar'

class EliminarElemento(DeleteView):
    model = Elemento
    template_name = 'nombre_del_template.html'
    success_url = '/donde_redirigir_despues_de_eliminar'

###################     Para LISTAR     ######################


class ListadoSede(ListView):
    model = Sede
    template_name = 'nombre_del_template.html'
    context_object_name = 'sedes'

class ListadoCategoria(ListView):
    model = Categoria
    template_name = 'nombre_del_template.html'
    context_object_name = 'categorias'

class ListadoElemento(ListView):
    model = Elemento
    template_name = 'nombre_del_template.html'
    context_object_name = 'elementos'