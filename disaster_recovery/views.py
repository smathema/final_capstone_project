from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import UserRegisterForm

class HomePage(TemplateView):
    template_name = "JobCode/index.html"

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'JobCode/register.html', {'form': form})
