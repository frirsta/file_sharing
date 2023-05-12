from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class File(models.Model):
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=100)


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'title')
