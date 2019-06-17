from django.urls import path
from .views import MachineListView, MachineDetailView, MachineCreateView, MachineUpdateView, MachineDeleteView


urlpatterns = [
    path('', MachineListView.as_view(), name='machine-list'),
    path('machinemgt/new/', MachineCreateView.as_view() , name='machine-create'),
    path('machinemgt/<int:pk>/update/', MachineUpdateView.as_view(), name='machine-update'),
    path('machinemgt/<int:pk>/delete/', MachineDeleteView.as_view(), name='machine-delete'),

]
