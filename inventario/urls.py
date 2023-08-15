from django.urls import path
from .views import *

app_name = 'inventario'

urlpatterns = [
    # URLs para Elemento
    path('elementos/', ElementoListView.as_view(), name='elemento-list'),
    path('elementos/create/', ElementoCreateView.as_view(), name='elemento-create'),
    path('elementos/update/<int:pk>/', ElementoUpdateView.as_view(), name='elemento-update'),
    path('elementos/delete/<int:pk>/', ElementoDeleteView.as_view(), name='elemento-delete'),

    # URLs para Sede
    path('sedes/', SedeListView.as_view(), name='sede-list'),
    path('sedes/create/', SedeCreateView.as_view(), name='sede-create'),
    path('sedes/update/<int:pk>/', SedeUpdateView.as_view(), name='sede-update'),
    path('sedes/delete/<int:pk>/', SedeDeleteView.as_view(), name='sede-delete'),
]