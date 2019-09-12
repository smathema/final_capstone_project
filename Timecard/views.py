from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView

from .models import Timesheet
from JobCode.models import Job
from MachineMgt.models import Machine


class TimesheetListView(LoginRequiredMixin, ListView):
    model = Timesheet


class TimesheetCreateView(LoginRequiredMixin, CreateView):
    model = Timesheet
    fields = ['site_code', 'contractor', 'date', 'total_hrs', 'total_amount', 'status']

    def get_context_data(self, **kwargs):
        data = super(TimesheetCreateView, self).get_context_data(**kwargs)
        job = Job.objects.values_list('job_code', 'hourly_rate')
        machine = Machine.objects.values_list('machine_code', 'hourly_rent')
        data['job'] = job
        data['machine'] = machine
        return data


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = request.POST
        mydict = dict(form.lists())
        hrs_list = [int(i) for i in mydict['mytext1']]
        hrs_sum = sum(hrs_list)
        droplist = []
<<<<<<< HEAD

        for i in mydict['dropdown1']:
            droplist.append(float(i))
        for i in mydict['dropdown2']:
            droplist.append(float(i))
=======
        if mydict.get('dropdown1'):  # if labor code information are added
            for i in mydict['dropdown1']:
                droplist.append(float(i))

        if mydict.get('dropdown2'):  # if machine code information are added
            for i in mydict['dropdown2']:
                droplist.append(float(i))
>>>>>>> c24ed4e59a62edaea8e8f0910cc3355c26d86fb2

        total_list = [x * y for x, y in zip(hrs_list, droplist)]
        total_sum = sum(total_list)

        ts = Timesheet()
        ts.site_code = mydict['site_code'][0]
        ts.date = mydict['date'][0]
        ts.contractor = mydict['contractor'][0]
        ts.total_hrs = hrs_sum
        ts.total_amount = total_sum
        ts.save()

<<<<<<< HEAD
    return redirect('/')
=======
    return redirect('/timecard')
>>>>>>> c24ed4e59a62edaea8e8f0910cc3355c26d86fb2


class TimesheetUpdateView(LoginRequiredMixin, UpdateView):
    model = Timesheet
    template_name = 'Timecard/timesheet_status.html'
    fields = ['status']
