from django.shortcuts import render, redirect
from accounts.auth import user_only
from services.models import Service
from .forms import FeedbackForm, AppointmentForm
from .models import Feedback, Category, Wishlist, Appointment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


@login_required
@user_only
# This function allows users to post their feedback through feedback form.
def post_feedback(request, category_id):
    category = Category.objects.get(id=category_id)
    user = request.user
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = request.POST
            feedback = data['feedback']
            rating = data['rating']
            fed = Feedback.objects.create(feedback=feedback, rating=rating, category=category, user=user)
            if fed:
                messages.add_message(request, messages.SUCCESS, 'Feedback posted successfully')
                return redirect('/services/show_category_services/' + str(category.id))
        else:
            messages.add_message(request, messages.ERROR, 'Unable to post feedback')
            return render(request, 'users/post_feedback.html', {'form_feedback': form})
    context = {
        'form_feedback': FeedbackForm,
        'activate_service': 'active'
    }
    return render(request, 'users/post_feedback.html', context)


@login_required
@user_only
# This function adds service to the wishlist.
def add_to_wishlist(request, service_id, category_id):
    category = Category.objects.get(id=category_id)
    user = request.user
    service = Service.objects.get(id=service_id)
    check_service_presence = Wishlist.objects.filter(user=user, service=service)
    if check_service_presence:
        messages.add_message(request, messages.ERROR, 'Service is already added')
        return redirect('/services/show_category_services/' + str(category.id))
    else:
        wishlist = Wishlist.objects.create(service=service, user=user)
        if wishlist:
            messages.add_message(request, messages.SUCCESS, " Item added to wishlist")
            return redirect('/users/my_wishlist')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add service to wishlist')


@login_required
@user_only
# This function returns the wishlist page consisting of all the services added to wishlist.
def show_wishlist_services(request):
    user = request.user
    wishlist_services = Wishlist.objects.filter(user=user)
    context = {
        'wishlist_services': wishlist_services,
        'activate_my_wishlist': 'active'
    }
    return render(request, 'users/my_wishlist.html', context)


@login_required
@user_only
# This function removes the services from user's wishlist
def remove_wishlist_item(request, wishlist_id):
    wishlist_service = Wishlist.objects.get(id=wishlist_id)
    wishlist_service.delete()
    messages.add_message(request, messages.SUCCESS, "Service removed successfully")
    return redirect('/users/my_wishlist')


@login_required
@user_only
# This function allows user to book appointments through appointment booking form
def appointment_form(request, service_id, wishlist_id):
    user = request.user
    service = Service.objects.get(id=service_id)
    wishlist_service = Wishlist.objects.get(id=wishlist_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            no_of_session = request.POST.get('no_of_session')
            cost = service.session_cost
            time = service.session_time
            session_time = int(no_of_session) * int(time)
            total_cost = int(no_of_session) * int(cost)
            contact_no = request.POST.get('contact_no')
            address = request.POST.get('address')
            appointment = Appointment.objects.create(
                service=service,
                user=user,
                no_of_session=no_of_session,
                session_time=session_time,
                total_cost=total_cost,
                contact_no=contact_no, address=address,
                status="Pending")
            if appointment:
                template = render_to_string('users/email_template.html',
                                            {'name': request.user.username, 'service': service.service_name})
                email = EmailMessage(
                    'Thank you for booking our services!!',
                    template,
                    settings.EMAIL_HOST_USER,
                    [request.user.email],
                )
                email.fail_silently = False
                email.send()
                messages.add_message(request, messages.SUCCESS, 'Appointment booked')
                wishlist_service.delete()
                return redirect('/users/my_appointment')

        else:
            messages.add_message(request, messages.ERROR, "Something went wrong")
            return render(request, 'users/appointment_form.html', {'appointment_form': form})
    context = {
        'appointment_form': AppointmentForm
    }
    return render(request, 'users/appointment_form.html', context)


@login_required
@user_only
# This function returns the appointments page consisting of user appointments
def my_appointment(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('-id')
    context = {
        'appointments': appointments,
        'activate_my_appointment': 'active'
    }
    return render(request, 'users/my_appointment.html', context)
