from django.contrib import admin
from django.db import models
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name','last_name')
    list_display_links = ('first_name',)
    search_fields =   ('username',)

admin.site.register(Registration, RegistrationAdmin)
