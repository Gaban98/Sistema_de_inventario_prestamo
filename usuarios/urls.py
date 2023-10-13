from django.urls import path
from .views import *
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('index/', index_view, name='index'),
    path('profesores/', UsuarioListView.as_view(), name='usuario-list'),
    path('profesores/sede/<int:sede_id>/', UsuarioListView.as_view(), name='usuario-list-sede'),  # Nueva ruta
    path('actualizar_profesor/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario-update'),
    path('eliminar_profesor/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario-delete'),

    ###############################3 LOGICA DEL PRESTAMO ##########################################

    path('prestamos/', views.listarcrear_prestamo, name='prestamo'),

    ##################################### alterar inventario ########################################
    path('devolver_prestamo/<int:prestamo_id>/', views.devolver_prestamo, name='devolver_prestamo'),
    path('historial_prestamos/', views.historial_prestamos, name='historial_prestamos'),
    path('api/elementos_por_categoria/<int:categoria_id>', views.elementos_por_categoria, name='elementos_por_categoria'),
    path('exportar_historial_prestamos_pdf/', views.exportar_historial_prestamos_pdf, name='exportar_historial_prestamos_pdf'),


]
