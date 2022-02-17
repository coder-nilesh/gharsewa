from django.test import SimpleTestCase
from django.urls import reverse,resolve
from users.views import *



class TestUrls(SimpleTestCase):
    def test_post_feedback_urls_is_resolved(self):
        url=reverse('post_feedback',args=[1])
        view=resolve(url).func
        self.assertEquals(view,post_feedback)

    def test_add_to_wishlist_urls_is_resolved(self):
        url=reverse('add_to_wishlist',args=[1,2])
        view=resolve(url).func
        self.assertEquals(view,add_to_wishlist)

    def test_show_wishlist_services_urls_is_resolved(self):
        url=reverse('show_wishlist_services')
        view=resolve(url).func
        self.assertEquals(view,show_wishlist_services)

    def test_remove_wishlist_item_urls_is_resolved(self):
        url=reverse('remove_wishlist_item',args=[1])
        view=resolve(url).func
        self.assertEquals(view,remove_wishlist_item)

    def test_appointment_form_urls_is_resolved(self):
        url=reverse('appointment_form',args=[1,2])
        view=resolve(url).func
        self.assertEquals(view,appointment_form)

    def test_my_appointment_urls_is_resolved(self):
        url=reverse('my_appointment')
        view=resolve(url).func
        self.assertEquals(view,my_appointment)

    
