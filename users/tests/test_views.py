from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def show_wishlist_services_get(self):
        client=Client()
        response=client.get(reverse('show_wishlist_services'))
        self.assertTemplateUsed(response,'users/my_wishlist.html')
    
    def test_my_appointment(self):
        client=Client()
        response=client.get(reverse('my_appointment'))
        self.assertTemplateNotUsed(response,'users/my_appointment.html')

    
