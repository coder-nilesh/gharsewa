import django_filters
from django.contrib.auth.models import User


class UserFilter(django_filters.FilterSet):
    username_contains = django_filters.CharFilter(field_name='username', label="Username",lookup_expr='icontains')

    class Meta:
        model = User
        fields = []


class AdminFilter(django_filters.FilterSet):
    username_contains = django_filters.CharFilter(field_name='username',label="Username" , lookup_expr='icontains')

    class Meta:
        model = User
        fields = []


