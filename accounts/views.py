import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from services.models import Category
from .forms import LoginForm, CreateUserForm, ProfileForm
from .auth import unauthenticated_user, user_only, admin_only
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


@user_only
# This function renders the homepage of the website.
def home_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'accounts/homepage.html', context)


@unauthenticated_user
# This function allows a user to register to the website.
def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username, email=user.email)
            messages.add_message(request, messages.SUCCESS, 'User registered successfully')
            return redirect('/login')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'accounts/register.html', {'form_register': form})
    context = {
        'form_register': CreateUserForm,
        'activate_register': 'active'
    }
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
# This function allows registered user to login to the a website.
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if not user.is_staff:
                    login(request, user)
                    return redirect('/')
                elif user.is_staff:
                    login(request, user)
                    return redirect('/admins')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid username or password')
                return render(request, 'accounts/login.html', {'form_login': form})
    context = {
        'form_login': LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/login.html', context)


@login_required
# This function allows logged in user to logout of the website.
def logout_user(request):
    logout(request)
    return redirect('/login')


@login_required
@user_only
# This function allows user to update their profile details.
def update_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        if request.FILES.get('profile_pic'):
            form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
            return redirect('/profile')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong username or password')
            return render(request, 'accounts/update_profile.html', {'form': form})
    context = {
        'form': ProfileForm(instance=profile),
        'activate_profile': 'active'
    }
    return render(request, 'accounts/update_profile.html', context)





@login_required
@user_only
# This function render the profile page of the user..
def profile(request):
    profile = request.user.profile
    context = {
        'form': ProfileForm(instance=profile),
        'activate_profile': 'active'
    }
    return render(request, 'accounts/profile.html', context)


@login_required
@admin_only
# This function allows admins to change their profile picture.
def password_change_admin(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password changed successfully")
            return redirect('/admins')
        else:
            messages.add_message(request, messages.ERROR, "Please verify the form fields")
            return render(request, 'accounts/password_change_admin.html', {'password_change_form': form})

    context = {
        'password_change_form': PasswordChangeForm(request.user)
    }
    return render(request, 'accounts/password_change_admin.html', context)


@login_required
@user_only
# This function allows users to change their password.
def password_change_user(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, "Password changed successfully")
            return redirect('/profile')
        else:
            messages.add_message(request, messages.ERROR, "Please verify the form fields")
            return render(request, 'accounts/password_change_user.html', {'password_change_form': form})

    context = {
        'password_change_form': PasswordChangeForm(request.user)
    }
    return render(request, 'accounts/password_change_user.html', context)
