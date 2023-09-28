from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from .models import *
from .form import *
from django.shortcuts import render, redirect, get_object_or_404



###################     Para EDITAR     ######################

class ActualizarSede(UpdateView):
    model = Sede
    fields = ['nombre', 'direccion', 'telefono', 'jefe_directo']
    template_name = 'SedeCategoria/editar_sede.html'
    success_url = reverse_lazy('inventario:listado_sedes')


class ActualizarCategoria(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'SedeCategoria/editar_categoria.html'
    success_url = reverse_lazy('inventario:listado_categorias')

class ActualizarElemento(UpdateView):
    model = Elemento
    fields = ['nombre', 'descripcion', 'estado', 'disponibilidad', 'sede', 'categoria']
    template_name = 'inventario/editar_elemento.html'
    success_url = reverse_lazy('inventario:listado_elementos')


###################     Para ELIMINAR   ######################

class EliminarSede(DeleteView):
    model = Sede
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('inventario:listado_sedes')

class EliminarCategoria(DeleteView):
    model = Categoria
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('inventario:listado_categorias')

class EliminarElemento(DeleteView):
    model = Elemento
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('inventario:listado_elementos')

###################     Para LISTAR   y AÑADIR   ######################
class ListadoSede(ListView):
    model = Sede
    template_name = 'SedeCategoria/listar_sede.html'
    context_object_name = 'sedes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_sede'] = SedeForm()  # Agregar el formulario al contexto
        return context
    def post(self, request, *args, **kwargs):
        form = SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario:listado_sedes')
        else:
            context = self.get_context_data()
            context['form_sede'] = form
            return self.render_to_response(context)
        
class ListadoCategoria(ListView):
    model = Categoria
    template_name = 'SedeCategoria/listar_categoria.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        return Categoria.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_categoria'] = CategoriaForm()  # Add the form to the context
        return context

    def post(self, request, *args, **kwargs):
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario:listado_categorias')
        else:
            context = self.get_context_data()
            context['form_categoria'] = form
            return self.render_to_response(context)

class ListadoElemento(ListView):
    model = Elemento
    template_name = 'inventario/listar_elemento.html'
    context_object_name = 'elementos'
    
    def post(self, request, *args, **kwargs):
        form = ElementoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario:listado_elementos')
        else:
            context = self.get_context_data()
            context['form_elemento'] = form
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_elemento'] = ElementoForm()
        context['form_filtro'] = FiltroElementosForm(self.request.GET)
        context['modal_url'] = reverse('inventario:listado_elementos')  # URL para el modal de creación
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        disponibilidad = self.kwargs.get('disponibilidad', None)
        if disponibilidad:
            queryset = queryset.filter(disponibilidad=disponibilidad)
        return queryset