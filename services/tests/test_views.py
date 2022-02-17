from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def test_get_category(self):
        client=Client()
        response=client.get(reverse('get_category'))
        self.assertTemplateNotUsed(response,'services/get_scategory.html')
   
    def test_get_category(self):
        client=Client()
        response=client.get(reverse('category_form'))
        self.assertTemplateNotUsed(response,'accounts/ocategory_form.html')

    def test_service_form(self):
        client=Client()
        response=client.get(reverse('service_form'))
        self.assertTemplateNotUsed(response,'services/oservice_form.html')

    def test_get_service(self):
        client=Client()
        response=client.get(reverse('get_service'))
        self.assertTemplateNotUsed(response,'services/get_service.html')

    def test_show_categories(self):
        client=Client()
        response=client.get(reverse('show_categories'))
        self.assertTemplateUsed(response,'services/show_categories.html')