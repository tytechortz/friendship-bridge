from django.db import models

member_types = [
    ('Core','Core Member'),
    ('Outer Core','Outer Core Member'),
    ('Events','Events Only Member'),
]

class Member(models.Model):
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    phone1 = models.CharField(max_length=12,blank=True)
    phone2 = models.CharField(max_length=12, blank=True)
    address1 = models.CharField(max_length=50,blank=True)
    address2 = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=25,blank=True)
    zipcode = models.CharField(max_length=5,blank=True)
    notes = models.TextField(blank=True)
    member_type = models.CharField(max_length=11, choices=member_types)

 

    def __str__(self):
        return self.first_name + " " + self.last_name


    


