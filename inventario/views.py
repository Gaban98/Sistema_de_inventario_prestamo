from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Elemento

class ElementoListView(ListView):
    model = Elemento
    template_name = 'inventario/elemento_list.html'
    context_object_name = 'elementos'

class ElementoCreateView(CreateView):
    model = Elemento
    template_name = 'inventario/elemento_form.html'
    fields = ['nombre', 'categoria', 'descripcion', 'disponible', 'estado', 'usuario', 'sede']

class ElementoUpdateView(UpdateView):
    model = Elemento
    template_name = 'inventario/elemento_form.html'
    fields = ['nombre', 'categoria', 'descripcion', 'disponible', 'estado', 'usuario', 'sede']

class ElementoDeleteView(DeleteView):
    model = Elemento
    template_name = 'inventario/elemento_confirm_delete.html'
    success_url = reverse_lazy('elemento-list')
