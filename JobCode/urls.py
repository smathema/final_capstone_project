from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView


urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('new/', JobCreateView.as_view(), name='job-create'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
]
