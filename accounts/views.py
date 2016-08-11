from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {"form":form})



