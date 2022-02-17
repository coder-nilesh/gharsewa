from django.test import SimpleTestCase
from accounts.forms import  ProfileForm


class TestForms(SimpleTestCase):
    def test_login_form(self):
        form=ProfileForm(data={
           'user':'',
           'username':'Nilesh',
           'email':'nileshkadel1@gmail.com',
           'firstname':'Nilesh',
           'lastname':'kadel',
           'phone':'9818668236',
           'address':'lokanthali',
           'profile_pic':'image.jpg'
            
        })
        self.assertTrue(form.is_valid())