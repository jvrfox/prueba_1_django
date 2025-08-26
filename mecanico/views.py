from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Mecanico

class MecanicoListView(ListView):
    model = Mecanico
    template_name = 'mecanico/mecanico_list.html'
    context_object_name = 'mecanicos'

class MecanicoDetailView(DetailView):
    model = Mecanico
    template_name = 'mecanico/mecanico_detail.html'

class MecanicoCreateView(CreateView):
    model = Mecanico
    fields = ['nombre', 'contacto', 'especialidad']
    template_name = 'mecanico/mecanico_form.html'
    success_url = reverse_lazy('mecanico_list')

class MecanicoUpdateView(UpdateView):
    model = Mecanico
    fields = ['nombre', 'contacto', 'especialidad']
    template_name = 'mecanico/mecanico_form.html'
    success_url = reverse_lazy('mecanico_list')

class MecanicoDeleteView(DeleteView):
    model = Mecanico
    template_name = 'mecanico/mecanico_confirm_delete.html'
    success_url = reverse_lazy('mecanico_list')