from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .form import *
from django.shortcuts import render, redirect

###################     Para AGREGAR    ######################

class CrearSede(CreateView):
    model = Sede
    fields = ['nombre', 'direccion', 'telefono', 'jefe_directo']
    template_name = 'SedeCategoria/crear_sede.html'
    success_url = 'SedeCategoria/listar_sede_categoria'

class CrearCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'SedeCategoria/listar_categoria.html'
    success_url = reverse_lazy('inventario:listado_categorias')

class CrearElemento(CreateView):
    model = Elemento
    fields = ['nombre', 'descripcion', 'estado', 'disponibilidad', 'sede', 'categoria']
    template_name = 'crear_elemento.html'
    success_url = 'inventario/listar_elemento'

###################     Para EDITAR     ######################

class ActualizarSede(UpdateView):
    model = Sede
    fields = ['nombre', 'direccion', 'telefono', 'jefe_directo']
    template_name = 'SedeCategoria/editar_sede.html'
    success_url = 'SedeCategoria/listar_sede_categoria'


class ActualizarCategoria(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'SedeCategoria/editar_categoria.html'
    success_url = reverse_lazy('inventario:listado_categorias')

class ActualizarElemento(UpdateView):
    model = Elemento
    fields = ['nombre', 'descripcion', 'estado', 'disponibilidad', 'sede', 'categoria']
    template_name = 'nombre_del_template.html'
    success_url = 'inventario/listar_elemento'

###################     Para ELIMINAR   ######################

class EliminarSede(DeleteView):
    model = Sede
    template_name = 'nombre_del_template.html'
    success_url = '/dSedeCategoria/listar_sede_categoria'

class EliminarCategoria(DeleteView):
    model = Categoria
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('inventario:listado_categorias')

class EliminarElemento(DeleteView):
    model = Elemento
    template_name = 'nombre_del_template.html'
    success_url = 'inventario/listar_elemento'

###################     Para LISTAR     ######################


class ListadoSede(ListView):
    model = Sede
    template_name = 'SedeCategoria/listar_sede.html'
    context_object_name = 'sedes'

class ListadoCategoria(ListView):
    model = Categoria
    template_name = 'SedeCategoria/listar_categoria.html'
    context_object_name = 'categorias'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_categoria'] = CategoriaForm()  # Agregar el formulario al contexto
        return context

class ListadoElemento(ListView):
    model = Elemento
    template_name = 'SedeCategoria/listar_elemento.html'
    context_object_name = 'elementos'