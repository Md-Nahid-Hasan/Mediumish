from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = UserCreationForm()
            return redirect('/')
    return render(request,'register.html', {'form': form})
