from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Members(models.Model):
    last_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.TextField()
    email = models.EmailField()
    phone1 = models.CharField(max_length=12)
    phone2 = models.CharField(max_length=12)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.TextField()
    zipcode = models.CharField(max_length=5)
    notes = models.TextField()
    core_member = models.BooleanField()
    outter_core_member = models.BooleanField()
    events_only_member = models.BooleanField()