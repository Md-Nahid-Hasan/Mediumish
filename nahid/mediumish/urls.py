from django.urls import path

from . import views

urlpatterns=[
    path("",views.index, name="index"),
    path("",views.story_list_view, name="story_list_view")
]