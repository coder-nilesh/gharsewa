from django.test import SimpleTestCase
from django.urls import reverse,resolve
from services.views import *


class TestUrls(SimpleTestCase):
    def test_get_category_urls_is_resolved(self):
        url=reverse('get_category')
        view=resolve(url).func
        self.assertEquals(view,get_category)

    def test_category_form_urls_is_resolved(self):
        url=reverse('category_form')
        view=resolve(url).func
        self.assertEquals(view,category_form)    

    def test_delete_category_urls_is_resolved(self):
        url=reverse('delete_category',args=[1])
        view=resolve(url).func
        self.assertEquals(view,delete_category)

    def test_get_service_urls_is_resolved(self):
        url=reverse('get_service')
        view=resolve(url).func
        self.assertEquals(view,get_service)

    def test_show_category_urls_is_resolved(self):
        url=reverse('show_categories')
        view=resolve(url).func
        self.assertEquals(view,show_categories)

    def test_get_appointment_urls_is_resolved(self):
        url=reverse('get_appointment')
        view=resolve(url).func
        self.assertEquals(view,get_appointment)

    def test_delete_service_urls_is_resolved(self):
        url=reverse('delete_service', args=[1])
        view=resolve(url).func
        self.assertEquals(view,delete_service)

    def test_get_category_services_urls_is_resolved(self):
        url=reverse('get_category_services', args=[1])
        view=resolve(url).func
        self.assertEquals(view,get_category_services)

    def test_update_category_urls_is_resolved(self):
        url=reverse('update_category', args=[1])
        view=resolve(url).func
        self.assertEquals(view,update_category)

    def test_service_form_urls_is_resolved(self):
        url=reverse('service_form')
        view=resolve(url).func
        self.assertEquals(view,service_form)

    def test_update_service_urls_is_resolved(self):
        url=reverse('update_service', args=[1])
        view=resolve(url).func
        self.assertEquals(view,update_service)

    
    

    



