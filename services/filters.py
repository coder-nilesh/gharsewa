import django_filters

from users.models import Appointment
from .models import Service, Category


class ServiceFilter(django_filters.FilterSet):
    service_contains = django_filters.CharFilter(field_name='service_name', label="Service name",
                                                 lookup_expr='icontains')
    class Meta:
        model = Service
        fields = []


class CategoryFilter(django_filters.FilterSet):
    category_contains = django_filters.CharFilter(field_name='category_name', label="Category name",
                                                  lookup_expr='icontains')
    class Meta:
        model = Category
        fields = []


class AppointmentFilter(django_filters.FilterSet):
    appointment_contains = django_filters.CharFilter(field_name='status', label="Appointment status",
                                                     lookup_expr='icontains')
    class Meta:
        model = Appointment
        fields = []


