from django.urls import path
from .views import JobListView, JobDetailView, JobCreateView, JobUpdateView, JobDeleteView


urlpatterns = [
    path('', JobListView.as_view(), name='job-list'),
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('jobcode/new/', JobCreateView.as_view(), name='job-create'),
    path('jobcode/<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('jobcode/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),

]
