from .models import Destination
from django.shortcuts import render

# Create your views here.

def index(request):
    object_list = Destination.objects.all()

    context = {
        'object_list':object_list
    }
    return render(request,"index.html", context)


