from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts.views import *


class TestUrls(SimpleTestCase):
    def test_home_page_urls_is_resolved(self):
        url=reverse('home_page')
        view=resolve(url).func
        self.assertEquals(view,home_page)

    def test_login_user_urls_is_resolved(self):
        url=reverse('login_user')
        view=resolve(url).func
        self.assertEquals(view,login_user)
    
    def test_register_user_urls_is_resolved(self):
        url=reverse('logout_user')
        view=resolve(url).func
        self.assertEquals(view,logout_user)

    def test_profile_urls_is_resolved(self):
        url=reverse('profile')
        view=resolve(url).func
        self.assertEquals(view,profile)

    def test_update_profile_urls_is_resolved(self):
        url=reverse('update_profile')
        view=resolve(url).func
        self.assertEquals(view,update_profile)

    def test_password_change_user_urls_is_resolved(self):
        url=reverse('home_page')
        view=resolve(url).func
        self.assertEquals(view,home_page)

    def test_password_change_user_urls_is_resolved(self):
        url=reverse('password_change_user')
        view=resolve(url).func
        self.assertEquals(view,password_change_user)

    def test_password_change_admin_urls_is_resolved(self):
        url=reverse('password_change_admin')
        view=resolve(url).func
        self.assertEquals(view,password_change_admin)



