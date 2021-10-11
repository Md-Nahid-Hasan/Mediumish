from django.contrib import admin
from django.db import models
from .models import Destination
from .models import Stories

# Register your models here.

class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading','user')
    list_display_links = ('heading',)
    search_fields =   ('heading',)

admin.site.register(Destination, DestinationAdmin)

class StoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading','user')
    list_display_links = ('heading',)
    search_fields =   ('heading',)

admin.site.register(Stories, StoriesAdmin)

