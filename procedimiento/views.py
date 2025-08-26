from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Procedimiento

class ProcedimientoListView(ListView):
    model = Procedimiento
    template_name = 'procedimiento/procedimiento_list.html'
    context_object_name = 'procedimientos'

class ProcedimientoDetailView(DetailView):
    model = Procedimiento
    template_name = 'procedimiento/procedimiento_detail.html'

class ProcedimientoCreateView(CreateView):
    model = Procedimiento
    fields = ['nombre', 'descripcion', 'mecanico', 'vehiculo']
    template_name = 'procedimiento/procedimiento_form.html'
    success_url = reverse_lazy('procedimiento_list')

class ProcedimientoUpdateView(UpdateView):
    model = Procedimiento
    fields = ['nombre', 'descripcion', 'mecanico', 'vehiculo']
    template_name = 'procedimiento/procedimiento_form.html'
    success_url = reverse_lazy('procedimiento_list')

class ProcedimientoDeleteView(DeleteView):
    model = Procedimiento
    template_name = 'procedimiento/procedimiento_confirm_delete.html'
    success_url = reverse_lazy('procedimiento_list')