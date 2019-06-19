from django.urls import path

from Timecard import views
from .views import TimesheetListView, TimesheetCreateView, TimesheetUpdateView


urlpatterns = [
    path('', TimesheetListView.as_view(), name='timesheet-list'),
    path('new/', TimesheetCreateView.as_view(), name='timesheet-create'),
    path('<int:pk>/update/', TimesheetUpdateView.as_view(), name='timesheet-update'),
    path('new/time', views.get_name, name='time'),
]
