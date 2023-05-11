from django.db import models
from django import forms

# Create your models here.


class File(models.Model):
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=100)


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'title')
