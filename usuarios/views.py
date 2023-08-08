from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Usuario

# Vista para listar los usuarios (solo para el administrador)
class UsuarioListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'

    def test_func(self):
        # Verifica si el usuario actual es el administrador
        return self.request.user.is_superuser

# Vista para crear un nuevo usuario (solo para el administrador)
class UsuarioCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Usuario
    template_name = 'usuarios/usuario_form.html'
    fields = ['nombre', 'correo', 'rol']  # Ajusta los campos según tu modelo

    def test_func(self):
        # Verifica si el usuario actual es el administrador
        return self.request.user.is_superuser

# Vista para editar un usuario existente (solo para el administrador)
class UsuarioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Usuario
    template_name = 'usuarios/usuario_form.html'
    fields = ['nombre', 'correo', 'rol']  # Ajusta los campos según tu modelo

    def test_func(self):
        # Verifica si el usuario actual es el administrador
        return self.request.user.is_superuser

# Vista para eliminar un usuario (solo para el administrador)
class UsuarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario-list')

    def test_func(self):
        # Verifica si el usuario actual es el administrador
        return self.request.user.is_superuser
