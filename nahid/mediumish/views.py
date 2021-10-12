from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Destination
from .models import Stories
from django.shortcuts import redirect, render
from account.login_forms import UserLoginForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login


def index(request):
    object_list = Destination.objects.all()
    story_object_list = Stories.objects.all()

    context = {
        'object_list':object_list,
        'story_object_list':story_object_list
    }
    return render(request,"index.html", context)

def story_list_view(request):
    story_object_list = Stories.objects.all()
    print('story_object_list', story_object_list)
    context = {
        'story_object_list':story_object_list
    }
    return render(request,"index.html", context)

def login_view(request):

    form = UserLoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request,f"Hello { user.username } ! You are logged in successfully")
                return redirect('index')
            else:
                messages.info(request,"Username or password error!")
                return render(request, "userlogin.html", {'form': form})
        else:
            messages.error(request,"Data not valid")
            return render(request, "userlogin.html", {'form': form})
    else:
        return render(request, "userlogin.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
