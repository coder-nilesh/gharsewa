from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def test_homepage(self):
        client=Client()
        response=client.get(reverse('home_page'))
        self.assertTemplateUsed(response,'accounts/homepage.html')
    
    def test_login(self):
        client=Client()
        response=client.get(reverse('login_user'))
        self.assertTemplateUsed(response,'accounts/login.html')

    def profile_test(self):
        client=Client()
        response=client.get(reverse('profile'))
        self.assertTemplateUsed(response,'accounts/profile.html')
    
