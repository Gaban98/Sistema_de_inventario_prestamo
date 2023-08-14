from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .models import Usuario
from django.contrib import messages

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

    def form_valid(self, form):
        cedula = form.cleaned_data['cedula']
        nombres = form.cleaned_data.get('nombres')
        apellidos = form.cleaned_data.get('apellidos')
        celular = form.cleaned_data.get('celular')

        if not str(cedula).isdigit():
            form.add_error('cedula', 'La cédula debe ser un número')
            return self.form_invalid(form)
        
        if not str(celular).isdigit():
            form.add_error('celular', 'El número celular debe ser un número')
            return self.form_invalid(form)

        if any(char.isdigit() for char in nombres):
            form.add_error('nombres', 'No se permiten números en los nombres.')
            return self.form_invalid(form)

        if any(char.isdigit() for char in apellidos):
            form.add_error('apellidos', 'No se permiten números en los apellidos.')
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hay errores en el formulario. Por favor, verifica los campos resaltados en rojo.')
        return super().form_invalid(form)



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

