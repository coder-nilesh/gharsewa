from django.db import models
from django.core import validators


class Category(models.Model):
    category_name = models.CharField(max_length=200, validators=[validators.MinLengthValidator(2)], null=True)
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='static/uploads/category-images', null=True)

    def __str__(self):
        return self.category_name


class Service(models.Model):
    service_name = models.CharField(max_length=200, validators=[validators.MinLengthValidator(2)], null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    service_description = models.TextField(null=True)
    session_time = models.IntegerField(null=True)
    image = models.FileField(upload_to='static/uploads/service-images', null=True)
    session_cost = models.FloatField(null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.service_name

