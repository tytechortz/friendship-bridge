from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    phone1 = models.CharField(max_length=12,blank=True)
    phone2 = models.CharField(max_length=12, blank=True)
    address1 = models.TextField(blank=True)
    address2 = models.TextField(blank=True)
    city = models.CharField(max_length=25,blank=True)
    zipcode = models.CharField(max_length=5,blank=True)
    notes = models.TextField(blank=True)
    core_member = models.BooleanField()
    outter_core_member = models.BooleanField()
    events_only_member = models.BooleanField()