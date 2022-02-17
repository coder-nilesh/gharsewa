from django.urls import path
from . import views

urlpatterns = [
    path('post_feedback/<int:category_id>', views.post_feedback,name='post_feedback'),

    path('add_to_wishlist/<int:service_id>/<int:category_id>', views.add_to_wishlist,name='add_to_wishlist'),
    path('my_wishlist', views.show_wishlist_services,name='show_wishlist_services'),
    path('remove_wishlist_service/<int:wishlist_id>', views.remove_wishlist_item,name='remove_wishlist_item'),

    path('appointment_form/<int:service_id>/<int:wishlist_id>', views.appointment_form,name='appointment_form'),
    path('my_appointment', views.my_appointment,name='my_appointment'),
]

