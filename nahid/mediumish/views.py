from .models import Destination
from .models import Stories
from django.shortcuts import render

# Create your views here.

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


