from django.db import models

# Create your models here.


class Requests(models.Model):
    title = models.CharField(max_length=100, blank=False)
    info = models.TextField(max_length=1000, blank=False)
    sender = models.CharField(max_length=100, blank=False)
    uploadDate = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    sponsorReqs = models.CharField(max_length=100, blank=False)
    sponsor = models.CharField(max_length=100, blank=False)


    def __str__(self):

        return self.title
