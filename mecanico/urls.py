from django.urls import path
from .views import (
    MecanicoListView,
    MecanicoDetailView,
    MecanicoCreateView,
    MecanicoUpdateView,
    MecanicoDeleteView,
)

urlpatterns = [
    path('', MecanicoListView.as_view(), name='mecanico_list'),
    path('<int:pk>/', MecanicoDetailView.as_view(), name='mecanico_detail'),
    path('nuevo/', MecanicoCreateView.as_view(), name='mecanico_create'),
    path('<int:pk>/editar/', MecanicoUpdateView.as_view(), name='mecanico_update'),
    path('<int:pk>/eliminar/', MecanicoDeleteView.as_view(), name='mecanico_delete'),
]
