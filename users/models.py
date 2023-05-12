from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.owner
    
