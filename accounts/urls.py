from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.home_page,name='home_page'),
    path ('login', views.login_user,name='login_user'),
    path('register', views.register_user,name='register_user'),
    path('logout', views.logout_user,name='logout_user'),

]


