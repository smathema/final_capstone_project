from django.urls import path
from .views import TimesheetListView, TimesheetCreateView, TimesheetUpdateView


urlpatterns = [
    path('', TimesheetListView.as_view(), name='timesheet-list'),
    path('timecard/new/',
         TimesheetCreateView.as_view(),
         name='timesheet-create'),
    path('timecard/<int:pk>/update/',
         TimesheetUpdateView.as_view(),
         name='timesheet-update'),
]
