from django import forms
from .models import Member




class MemberForm(forms.ModelForm):
    ## configuration details, available on every instance
    class Meta:
        model = Member
        fields = ('last_name', 'first_name', 'email', 'phone1', 'phone2',
        'address1', 'address2', 'city', 'zipcode','notes','member_type')




    