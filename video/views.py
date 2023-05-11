from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import File, FileForm

# Create your views here.


class FileCreateView(CreateView):
    model = File
    form_class = FileForm
    template_name = 'upload.html'
    success_url = reverse_lazy('files')


class FileListView(ListView):
    model = File
    template_name = 'files.html'
    context_object_name = 'files'


def download(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    response = HttpResponse(file.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
    return response
