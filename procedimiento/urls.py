from django.urls import path
from .views import (
    ProcedimientoListView,
    ProcedimientoDetailView,
    ProcedimientoCreateView,
    ProcedimientoUpdateView,
    ProcedimientoDeleteView,
)

urlpatterns = [
    path('', ProcedimientoListView.as_view(), name='procedimiento_list'),
    path('<int:pk>/', ProcedimientoDetailView.as_view(), name='procedimiento_detail'),
    path('nuevo/', ProcedimientoCreateView.as_view(), name='procedimiento_create'),
    path('<int:pk>/editar/', ProcedimientoUpdateView.as_view(), name='procedimiento_update'),
    path('<int:pk>/eliminar/', ProcedimientoDeleteView.as_view(), name='procedimiento_delete'),
]
