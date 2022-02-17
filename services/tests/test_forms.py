from django.test import SimpleTestCase
from services.forms import  *


class TestForms(SimpleTestCase):
    def test_category_form(self):
        form=CategoryForm(data={
            'category_name':'plumbing',
            'description':"hello i am plumber",
            'image':'image1.jpg'
        })
        self.assertTrue(form.is_valid())

    def test_category_form(self):
        form=CategoryForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)


    


