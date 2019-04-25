from django.db import models

member_types = [
    ('Core','Core Member'),
    ('Outer Core','Outer Core Member'),
    ('Events','Events Only Member'),
]

class Member(models.Model):
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    email = models.EmailField(blank=True,null=True)
    phone1 = models.CharField(max_length=12,blank=True,null=True)
    phone2 = models.CharField(max_length=12, blank=True,null=True)
    address1 = models.CharField(max_length=50,blank=True,null=True)
    address2 = models.CharField(max_length=50,blank=True,null=True)
    city = models.CharField(max_length=25,blank=True,null=True)
    zipcode = models.CharField(max_length=5,blank=True,null=True)
    notes = models.TextField(blank=True,null=True)
    member_type = models.CharField(max_length=11, choices=member_types,null=True)

 

    def __str__(self):
        return self.first_name + " " + self.last_name


    


