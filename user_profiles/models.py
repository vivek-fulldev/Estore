from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
class Anonmyous_User(models.Model):
    user_id = models.CharField(max_length=50,unique=True)
    active_status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user_id
    
class Registration(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_no = PhoneNumberField(unique=True)
    email_address =  models.EmailField(max_length=40,unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name="Registered User"
        verbose_name_plural="Registered Users"
