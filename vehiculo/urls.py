from django.urls import path
from .views import (
    VehiculoListView,
    VehiculoDetailView,
    VehiculoCreateView,
    VehiculoUpdateView,
    VehiculoDeleteView,
)

urlpatterns = [
    path('', VehiculoListView.as_view(), name='vehiculo_list'),
    path('<str:pk>/', VehiculoDetailView.as_view(), name='vehiculo_detail'),
    path('nuevo/', VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('<str:pk>/editar/', VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('<str:pk>/eliminar/', VehiculoDeleteView.as_view(), name='vehiculo_delete'),
]
