from django.urls import path
from mediumish.views import login_view
from mediumish.views import logout_view

from . import views

urlpatterns=[
    path("register/",views.register, name="register"),
    path("custom/login/",login_view, name="account_login"),
    path("logout/",logout_view, name="userlogout")

]