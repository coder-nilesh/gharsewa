from django.shortcuts import render, redirect
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from accounts.forms import CreateUserForm
from accounts.models import Profile
from services.models import Service
from django.contrib import messages

from users.models import Appointment
from .filters import UserFilter, AdminFilter


@login_required
@admin_only
# This function renders the admin dashboard page.
def admin_dashboard(request):
    user = User.objects.filter(is_staff=0)
    user_count = user.count()
    admin = User.objects.filter(is_staff=1)
    admin_count = admin.count()
    service = Service.objects.all()
    service_count = service.count()
    appointment = Appointment.objects.all()
    appointment_count = appointment.count()
    context = {
        'user': user_count,
        'admin': admin_count,
        'service': service_count,
        'appointment': appointment_count,
        'activate_dashboard': 'active'
    }
    return render(request, 'admins/homepage-admin.html', context)


# @login_required
# @admin_only
# This function allows admin to view all the registered users.
def show_users(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    user_filter = UserFilter(request.GET, queryset=users)
    users_final = user_filter.qs
    context = {
        'users': users_final,
        'activate_users': 'active',
        'user_filter': user_filter
    }
    return render(request, 'admins/show_users.html', context)


@login_required
@admin_only
# This function allows admin to view other list of admins of the website.
def show_admins(request):
    admins = User.objects.filter(is_staff=1).order_by('-id')
    admin_filter = AdminFilter(request.GET, queryset=admins)
    admins_final = admin_filter.qs
    context = {
        'admins': admins_final,
        'activate_admins': 'active',
        'admin_filter': admin_filter
    }
    return render(request, 'admins/show_admins.html', context)


@login_required
@admin_only
# This function allows admin to promote a registered user to an admin.
def promote_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User promoted to admin')
    return redirect('/admins/view_admins')


@login_required
@admin_only
# This function allows admin to demote an admin to just a user.
def demote_admin(request, user_id):
    admin = User.objects.get(id=user_id)
    admin.is_staff = False
    admin.save()
    messages.add_message(request, messages.SUCCESS, 'Admin denoted to user')
    return redirect('/admins/view_users')


@login_required
@admin_only
# This function allows admin to register a user from admin panel.
def register_user_by_admin(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, username=user.username, email=user.email)
            messages.add_message(request, messages.SUCCESS, 'User registered successfully')
            return redirect('/admins/view_users')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'admins/register_user.html', {'form_register': form})
    context = {
        'form_register': CreateUserForm,
    }
    return render(request, 'admins/register_user.html', context)