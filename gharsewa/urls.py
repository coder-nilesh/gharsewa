from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),
    path('admins/', include('admins.urls')),
    path('services/', include('services.urls')),
    path('users/', include('users.urls'))
]

