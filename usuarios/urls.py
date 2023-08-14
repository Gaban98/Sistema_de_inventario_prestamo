from django.urls import path
from .views import *

urlpatterns = [
    path('', UsuarioListView.as_view(), name='usuario-list'),
    path('create/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('update/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('delete/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario-delete'),
]
