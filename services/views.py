import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.auth import admin_only
from users.models import Appointment, Feedback
from .forms import ServiceForm, CategoryForm
from django.contrib import messages
from .models import Service, Category
from .filters import ServiceFilter, CategoryFilter, AppointmentFilter


@login_required
@admin_only
# This function renders the categories page of admin panel with all the categories.
def get_category(request):
    categories = Category.objects.all().order_by('-id')

    category_filter = CategoryFilter(request.GET, queryset=categories)
    category_final = category_filter.qs
    context = {
        'categories': category_final,
        'activate_category': 'active',
        'category_filter': category_filter
    }
    return render(request, 'services/get_category.html', context)


@login_required
@admin_only
# This function allows admin to add categories through category form.
def category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect('/services/get_category')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'accounts/category_form.html', {'form_category': form})
    context = {
        'form_category': CategoryForm,
        'activate_category': 'active'
    }
    return render(request, 'services/category_form.html', context)


@login_required
@admin_only
# This function allows admin to delete a category.
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category deleted successfully')
    return redirect('/services/get_category')


@login_required
@admin_only
# This function allows admin to update category details.
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST,request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Category updated successfully")
            return redirect("/services/get_category")
        else:
            messages.add_message(request, messages.ERROR, "Unable to update category")
            return redirect(request, "services/category_update_form.html", {'form_category': form})
    context = {
        'form_category': CategoryForm(instance=category),
        'activate_category': 'active'
    }
    return render(request, 'services/category_update_form.html', context)


@login_required
@admin_only
# This function allows admin to view all the added services of the a category.
def get_category_services(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {
        'category': category
    }
    return render(request, 'services/get_category_services.html', context)


@login_required
@admin_only
# This function allows admin to add a service through service category form.
def service_form(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Service added successfully')
            return redirect('/services/get_service')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add service')
            return render(request, 'services/service_form.html', {'form_service': form})
    context = {
        'form_service': ServiceForm,
        'activate_service': 'active'
    }
    return render(request, 'services/service_form.html', context)


@login_required
@admin_only
# This function returns the service page of admin panel consisting of all the added services.
def get_service(request):
    services = Service.objects.all().order_by('-id')
    service_filter = ServiceFilter(request.GET, queryset=services)
    services_final = service_filter.qs
    context = {
        'services': services_final,
        'activate_service': 'active',
        'service_filter': service_filter
    }
    return render(request, 'services/get_service.html', context)


@login_required
@admin_only
# This function allows admin to delete a service.
def delete_service(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    messages.add_message(request, messages.SUCCESS, 'Service deleted successfully')
    return redirect('/services/get_service')


@login_required
@admin_only
# This function allows admin to update the details of a service.
def update_service(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == "POST":
        if request.FILES.get('image'):
            os.remove(service.image.path)
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Service updated successfully")
            return redirect("/services/get_service")
        else:
            messages.add_message(request, messages.ERROR, "Unable to update service")
            return redirect(request, "services/service_update_form.html", {'form_service': form})
    context = {
        'form_service': ServiceForm(instance=service),
        'activate_service': 'active'
    }
    return render(request, 'services/service_update_form.html', context)


@login_required
@admin_only
# This function renders the appointment page of admin panel with all the booked appointments.
def get_appointment(request):
    appointments = Appointment.objects.all().order_by('-id')
    appointment_filter = AppointmentFilter(request.GET, queryset=appointments)
    appointment_final = appointment_filter.qs
    context = {
        'appointments': appointment_final,
        'activate_appointment': 'active',
        'appointment_filter': appointment_filter
    }
    return render(request, 'services/get_appointment.html', context)


@login_required
@admin_only
# This function allows admin to delete an appointment.
def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    messages.add_message(request, messages.SUCCESS, 'Appointment deleted successfully')
    return redirect('/services/get_appointment')


@login_required
@admin_only
# This function allows admin to update the status of the appointment.
def update_appointment_status(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.status = "Completed"
    appointment.save()
    messages.add_message(request, messages.SUCCESS, 'Status changed to Completed')
    return redirect('/services/get_appointment')


# This function renders categories page on the user side.
def show_categories(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'activate_services': 'active'
    }
    return render(request, 'services/show_categories.html', context)


# This function renders the services of a selected category on the user side.
def show_category_services(request, category_id):
    category = Category.objects.get(id=category_id)
    feedback = Feedback.objects.filter(category=category)
    context = {
        'category': category,
        'activate_services': 'active',
        'feedbacks': feedback
    }
    return render(request, 'services/show_category_services.html', context)