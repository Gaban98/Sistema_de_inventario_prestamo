from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Elemento, Sede

# Vista para listar los elementos
class ElementoListView(ListView):
    model = Elemento
    template_name = 'inventario/elemento_list.html'
    context_object_name = 'elementos'

# Vista para crear un nuevo elemento
class ElementoCreateView(SuccessMessageMixin, CreateView):
    model = Elemento
    template_name = 'inventario/elemento_form.html'
    fields = ['nombre', 'categoria', 'descripcion', 'estado', 'disponible']
    success_url = reverse_lazy('elemento-list')
    success_message = 'Elemento creado exitosamente.'

# Vista para editar un elemento existente
class ElementoUpdateView(SuccessMessageMixin, UpdateView):
    model = Elemento
    template_name = 'inventario/elemento_form.html'
    fields = ['nombre', 'categoria', 'descripcion', 'estado', 'disponible']
    success_url = reverse_lazy('elemento-list')
    success_message = 'Elemento actualizado exitosamente.'

# Vista para eliminar un elemento
class ElementoDeleteView(DeleteView):
    model = Elemento
    template_name = 'inventario/elemento_confirm_delete.html'
    success_url = reverse_lazy('elemento-list')


    ############### `ACA VAN LAS VISTAS DE SEDE  ############`

# Vista para listar las sedes
class SedeListView(ListView):
    model = Sede
    template_name = 'inventario/sede_list.html'
    context_object_name = 'sedes'

# Vista para crear una nueva sede
class SedeCreateView(SuccessMessageMixin, CreateView):
    model = Sede
    template_name = 'inventario/sede_form.html'
    fields = ['nombre', 'direccion', 'celular_jefe']
    success_url = reverse_lazy('sede-list')
    success_message = 'Sede creada exitosamente.'

# Vista para editar una sede existente
class SedeUpdateView(SuccessMessageMixin, UpdateView):
    model = Sede
    template_name = 'inventario/sede_form.html'
    fields = ['nombre', 'direccion', 'celular_jefe']
    success_url = reverse_lazy('sede-list')
    success_message = 'Sede actualizada exitosamente.'

# Vista para eliminar una sede
class SedeDeleteView(DeleteView):
    model = Sede
    template_name = 'inventario/sede_confirm_delete.html'
    success_url = reverse_lazy('sede-list')
