from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Destination(models.Model):
    img = models.ImageField(upload_to='uploads/')
    heading = models.CharField(max_length=100)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.heading)

class Stories(models.Model):
    img = models.ImageField(upload_to='uploads/')
    heading = models.CharField(max_length=100)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.heading)

