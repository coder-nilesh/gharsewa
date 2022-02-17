from django import forms
from django.forms import ModelForm
from .models import Feedback, Appointment


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback', 'rating']


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['no_of_session', 'contact_no', 'address']
