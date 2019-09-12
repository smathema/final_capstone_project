from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Machine
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class MachineListView(LoginRequiredMixin, ListView):
    model = Machine


class MachineDetailView(LoginRequiredMixin, DetailView):
    model = Machine


class MachineCreateView(LoginRequiredMixin, CreateView):
    model = Machine
    fields = ['machine_code', 'description', 'hourly_rent', 'max_hour_per_day']


class MachineUpdateView(LoginRequiredMixin, UpdateView):
    model = Machine
    fields = ['machine_code', 'description', 'hourly_rent', 'max_hour_per_day']


class MachineDeleteView(LoginRequiredMixin, DeleteView):
    model = Machine
    success_url = '/machinemgt'
