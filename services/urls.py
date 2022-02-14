from django.urls import path
from . import views

urlpatterns = [
    path('get_category', views.get_category, name='get_category'),
    path('category_form', views.category_form, name='category_form'),
    path('delete_category/<int:category_id>', views.delete_category, name="delete_category"),
    path('update_category/<int:category_id>', views.update_category,name='update_category'),
    path('get_category_services/<int:category_id>', views.get_category_services,name='get_category_services'),

    path('service_form', views.service_form,name='service_form'),
    path('get_service', views.get_service, name="get_service"),
    path('delete_service/<int:service_id>', views.delete_service, name='delete_service'),
    path('update_service/<int:service_id>', views.update_service, name='update_service'),

    path('get_appointment', views.get_appointment, name='get_appointment'),
    path('delete_appointment/<int:appointment_id>', views.delete_appointment),
    path('update_appointment_status/<int:appointment_id>', views.update_appointment_status),

    path('show_categories', views.show_categories, name="show_categories"),
    path('show_category_services/<int:category_id>', views.show_category_services),

    ]