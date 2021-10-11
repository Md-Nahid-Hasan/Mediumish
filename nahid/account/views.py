from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib import messages

def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request,'register.html', {'form': form})
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration Successfull")
            return redirect('index')
        else:
            print("Invalid Form")
            print(form.errors)
            return render(request,'register.html',
            {
                'form': form,
                'form_errors': form.errors
            })
    
   
