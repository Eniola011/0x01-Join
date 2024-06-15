from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

# Create your views here.

def home(request):
    """ HomePage """
    context = {
        'user': request.user
    }
    return render(request, 'home.html', context)

def login(request):
    # login logic
    return render(request, 'registration/login.html')

def signup(request):
    # signup logic
    return render(request, 'registration/signup.html')
