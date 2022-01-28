from django.shortcuts import render, redirect
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from accounts.forms import CreateUserForm
from accounts.models import Profile
from services.models import *
from django.contrib import messages

from users.models import Appointment
from .filters import UserFilter, AdminFilter


# @login_required
# @admin_only
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