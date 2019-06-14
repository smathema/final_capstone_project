from django.urls import path
from .views import MachineListView, MachineDetailView, MachineCreateView, MachineUpdateView, MachineDeleteView


urlpatterns = [
    path('',MachineListView.as_view() , name='machine-list'),
    path('machine/<int:pk>/',MachineDetailView.as_view() , name='machine-detail'),
    path('machine/new/',MachineCreateView.as_view() , name='machine-create'),
    path('machine/<int:pk>/update/',MachineUpdateView.as_view() , name='machine-update'),
    path('machine/<int:pk>/delete/',MachineDeleteView.as_view() , name='machine-delete'),

]
