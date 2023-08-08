from django.urls import path
from .views import ElementoListView, ElementoCreateView, ElementoUpdateView, ElementoDeleteView

urlpatterns = [
    path('', ElementoListView.as_view(), name='elemento-list'),
    path('create/', ElementoCreateView.as_view(), name='elemento-create'),
    path('update/<int:pk>/', ElementoUpdateView.as_view(), name='elemento-update'),
    path('delete/<int:pk>/', ElementoDeleteView.as_view(), name='elemento-delete'),
]
