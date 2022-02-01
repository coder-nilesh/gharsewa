from django import forms
from django.forms import ModelForm
from .models import Service, Category


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


