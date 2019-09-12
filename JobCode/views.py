from . models import Job
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class JobListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Job


class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    fields = ['job_code', 'description', 'hourly_rate', 'max_hour_per_day']


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ['job_code', 'description', 'hourly_rate', 'max_hour_per_day']


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    success_url = '/jobcode'
