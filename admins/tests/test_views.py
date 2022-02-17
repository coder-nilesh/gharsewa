from django.test import TestCase,Client
from django.urls import reverse


class Test_views(TestCase):
    def testadmindashboard_get(self):
        client=Client()
        response=client.get(reverse('admin_dashboard'))
        # self.assertEquals(response.status_code,200)
        self.assertTemplateNotUsed(response,'admins/homepage-admin.html')

    def show_user_get(self):
        client=Client()
        response=client.get(reverse('show_user'))
        self.assertTemplateUsed(response,'admins/show_users.html')

    def show_admin_get(self):
        client=Client()
        response=client.get(reverse('show_admin'))
        self.assertTemplateUsed(response,'admins/show_admins.html')

    

