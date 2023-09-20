from django.urls import path
from .views import *
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('index/', index_view, name='index'),
    path('profesores/', UsuarioListView.as_view(), name='usuario-list'),
    path('actualizar_profesor/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('eliminar_profesor/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario-delete'),

    ###############################3 LOGICA DEL PRESTAMO ##########################################

    path('prestamos/', views.listarcrear_prestamo, name='prestamo'),

    ##################################### alterar inventario ########################################
path('devolver_prestamo/<int:prestamo_id>/', views.devolver_prestamo, name='devolver_prestamo'),

    
]
