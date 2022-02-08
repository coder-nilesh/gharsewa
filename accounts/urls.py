from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.home_page,name='home_page'),
    path ('login', views.login_user,name='login_user'),
    path('register', views.register_user,name='register_user'),
    path('logout', views.logout_user,name='logout_user'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('password_change_user', views.password_change_user, name='password_change_user'),
    path('password_change_admin', views.password_change_admin, name='password_change_admin'),

]


