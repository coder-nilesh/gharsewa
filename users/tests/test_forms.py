from django.test import SimpleTestCase
from users.forms import  *


class TestForms(SimpleTestCase):

    # Test for feedback_form
    def test_feedback_form(self):
        form=FeedbackForm(data={
            'category_name':'plumbing',
            'user':"Nilesh",
            'feedback':'Good sevices',
            'rating':'5'
        })      
        self.assertTrue(form.is_valid())

     # Test for appointment_form
    def test_apponitment_form(self):
        form=AppointmentForm(data={
            'servicee':'painting wall',
            'user':"Nilesh",
            'no_of_session':'2',
            'session-time':'60 min',
            'total_cost':'5000',
            'status':'pending',
            'contact_no':'9840026546',
            'address':'lokanthali Bhaktapur',


        })      
        self.assertTrue(form.is_valid())

            