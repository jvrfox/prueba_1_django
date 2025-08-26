from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vehiculo

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_list.html'
    context_object_name = 'vehiculos'

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_detail.html'

class VehiculoCreateView(CreateView):
    model = Vehiculo
    fields = ['patente', 'modelo', 'anio', 'dueno']
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    fields = ['modelo', 'anio', 'dueno']
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculo_list')