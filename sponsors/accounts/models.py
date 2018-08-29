
from django.db import models


# Create your models here.


class Sponsor(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=True)
    birth_date = models.DateField(null=True)
    number = models.CharField(max_length=12, blank=False)
    city = models.CharField(max_length=50, blank=True)
    img = models.FileField(upload_to='docs/', blank=False)
    work = models.CharField(max_length=100, blank=False)
    work_locations = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=100, blank=False)
    success = models.BooleanField(default=False)
    up_date = models.DateField(auto_now_add=True)
    type_user = models.CharField(max_length=50, default='sponsor')

    def __str__(self):

        return self.full_name

