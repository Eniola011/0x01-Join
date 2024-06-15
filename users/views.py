from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.

def home(request):
    """ Homepage """
    return render(request, 'homepage.html')

def login_signup(request):
    """ combined login and signup logic """
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        elif 'signup' in request.POST:
            form = CustomUserCreationForm(request.POST)  # or NewUserForm
            if form.is_valid():
                form.save()
                messages.success(request, 'You have successfully signed up. Please log in.')
                return redirect('login_signup')
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()  # or NewUserForm

    return render(request, 'sign.html', {'form': form})
