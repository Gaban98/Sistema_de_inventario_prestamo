from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *


########################### CATEGIRIAS #######################################
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'inventario/listar_categorias.html'
    context_object_name = 'categorias'

class CategoriaCreateView(SuccessMessageMixin, CreateView):
    model = Categoria
    template_name = 'inventario/crear_categoria.html'
    fields = ['nombre']
    success_url = reverse_lazy('categoria-list')
    success_message = 'Categoría creada exitosamente.'

class CategoriaUpdateView(SuccessMessageMixin, UpdateView):
    model = Categoria
    template_name = 'inventario/editar_categoria.html'
    fields = ['nombre']
    success_url = reverse_lazy('categoria-list')
    success_message = 'Categoría actualizada exitosamente.'

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'inventario/eliminar_categoria.html'
    success_url = reverse_lazy('categoria-list')

########################### SEDES #######################################

class SedeListView(ListView):
    model = Sede
    template_name = 'inventario/listar_sedes.html'
    context_object_name = 'sedes'

class SedeCreateView(SuccessMessageMixin, CreateView):
    model = Sede
    template_name = 'inventario/crear_sede.html'
    fields = ['nombre', 'direccion', 'telefono', 'jefe_directo']
    success_url = reverse_lazy('sede-list')
    success_message = 'Sede creada exitosamente.'

class SedeUpdateView(SuccessMessageMixin, UpdateView):
    model = Sede
    template_name = 'inventario/editar_sede.html'
    fields = ['nombre', 'direccion', 'telefono', 'jefe_directo']
    success_url = reverse_lazy('sede-list')
    success_message = 'Sede actualizada exitosamente.'

class SedeDeleteView(DeleteView):
    model = Sede
    template_name = 'inventario/eliminar_sede.html'
    success_url = reverse_lazy('sede-list')

########################### DISPONIBILIDADES #######################################

class DisponibilidadListView(ListView):
    model = Disponibilidad
    template_name = 'inventario/listar_disponibilidades.html'
    context_object_name = 'disponibilidades'

############################ ELEMENTOS #####################################
class ElementoListView(ListView):
    model = Elemento
    template_name = 'inventario/listar_elementos.html'
    context_object_name = 'elementos'

class ElementoCreateView(SuccessMessageMixin, CreateView):
    model = Elemento
    template_name = 'inventario/crear_elemento.html'
    fields = ['nombre', 'descripcion', 'estado', 'disponibilidad', 'sede', 'categoria']
    success_url = reverse_lazy('elemento-list')
    success_message = 'Elemento creado exitosamente.'

class ElementoUpdateView(SuccessMessageMixin, UpdateView):
    model = Elemento
    template_name = 'inventario/editar_elemento.html'
    fields = ['nombre', 'descripcion', 'estado', 'disponibilidad', 'sede', 'categoria']
    success_url = reverse_lazy('elemento-list')
    success_message = 'Elemento actualizado exitosamente.'

class ElementoDeleteView(DeleteView):
    model = Elemento
    template_name = 'inventario/eliminar_elemento.html'
    success_url = reverse_lazy('elemento-list')

# Resto de las vistas para crear, actualizar y eliminar Disponibilidad y Elemento...
