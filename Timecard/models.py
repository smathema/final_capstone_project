from django.db import models
from django.urls import reverse
import datetime


class Timesheet(models.Model):
    site_code = models.CharField(max_length=20)
    contractor = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    total_hrs = models.PositiveIntegerField()
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.site_code)

    def get_absolute_url(self):
        return reverse('timesheet-list')
