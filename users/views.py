from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successfull')
            return redirect('login')
        messages.error(request, 'Unsuccessfull')
    form = NewUserForm()
    return render(request=request, template_name='register.html', context={'register_form': form})

