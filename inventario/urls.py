from django.urls import path
from .views import *

app_name = 'inventario'

urlpatterns = [

    ########## CREADORES #################
    path('crear_sede/', CrearSede.as_view(), name='crear_sede'),
    path('crear_categoria/', CrearCategoria.as_view(), name='crear_categoria'),
    path('crear_elemento/', CrearElemento.as_view(), name='crear_elemento'),

############# EDITORES #################
    path('actualizar_sede/<int:pk>/', ActualizarSede.as_view(), name='actualizar_sede'),
    path('actualizar_categoria/<int:pk>/', ActualizarCategoria.as_view(), name='actualizar_categoria'),
    path('actualizar_elemento/<int:pk>/', ActualizarElemento.as_view(), name='actualizar_elemento'),


############# ELIMINADORES #################
    path('eliminar_sede/<int:pk>/', EliminarSede.as_view(), name='eliminar_sede'),
    path('eliminar_categoria/<int:pk>/', EliminarCategoria.as_view(), name='eliminar_categoria'),
    path('eliminar_elemento/<int:pk>/', EliminarElemento.as_view(), name='eliminar_elemento'),


############# LISTADORES #################
    path('sedes/', ListadoSede.as_view(), name='listado_sedes'),
    path('categorias/', ListadoCategoria.as_view(), name='listado_categorias'),
    path('elementos/', ListadoElemento.as_view(), name='listado_elementos'),
]