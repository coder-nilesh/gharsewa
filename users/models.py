from django.db import models
from django.core import validators
from services.models import Category
from django.contrib.auth.models import User
from services.models import Service


class Feedback(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    feedback = models.TextField(validators=[validators.MinLengthValidator(5)])
    rating = models.IntegerField(validators=[validators.MaxValueValidator(10)])
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback


class Wishlist(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)


class Appointment(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    service = models.ForeignKey(Service, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    no_of_session = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    session_time = models.IntegerField(null=True)
    total_cost = models.IntegerField(null=True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    contact_no = models.CharField(validators=[validators.MinLengthValidator(9), validators.MaxLengthValidator(10)],
                                  null=True, max_length=10)
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
