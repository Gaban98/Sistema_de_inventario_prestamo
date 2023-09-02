from django.urls import path
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('index/', index_view, name='index'),
    path('profesores/', UsuarioListView.as_view(), name='usuario-list'),
    path('actualizar_profesor/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('eliminar_profesor/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario-delete'),
]
