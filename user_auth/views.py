from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # Import messages for feedback
from django.http import HttpResponseRedirect
from django.urls import reverse

def user_login(request):
    """
    Render the user login page.
    """
    return render(request, 'registration/login.html')

def authenticate_user(request):
    """
    Authenticate a user based on the provided username and password.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid username or password.')  # Add error message
            return redirect('user_auth:login')  # Redirect to login on failure
        else:
            login(request, user)
            return redirect('user_auth:user_view')  # Redirect to user profile after successful login
    return redirect('user_auth:login')  # Redirect GET requests to login

def show_user(request):
    """
    Display the user's profile page.
    """
    if request.user.is_authenticated:
        return render(request, 'registration/user.html', {
            "username": request.user.username,
            # Do not expose the password for security reasons
        })
    else:
        return redirect('user_auth:login')  # Redirect unauthenticated users to login

def register(request):
    """
    Handle user registration, including form validation and user creation.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('polls:index')  # Redirect to the desired page after successful registration
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')  # Add error message
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
