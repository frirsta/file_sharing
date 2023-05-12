from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from .models import File, FileForm

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class HomePageView(ListView):
    template_name = 'home.html'
    queryset = File.objects.all()


class FileCreateView(CreateView):
    model = File
    form_class = FileForm
    template_name = 'upload.html'
    success_url = reverse_lazy('files')


class FileListView(ListView):
    model = File
    template_name = 'files.html'
    context_object_name = 'files'
    queryset = File.objects.all()
    


class FileDetailView(DetailView):
    model = File

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        file = get_object_or_404(File, pk=pk)
        context["file"] = File.objects.all()
        return context


def download(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    response = HttpResponse(file.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
    return response
