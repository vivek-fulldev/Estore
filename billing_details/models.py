from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from user_profiles.models import Anonmyous_User

# Create your models here.
CITIES = [
    ('None', 'None'),
    ('Mumbai', 'Mumbai'),
    ('Bangalore', 'Bangalore'),
    ('Delhi', 'Delhi'),
]
PAYEMENT_TYPE= [
    ('cod', 'Cash On Delivery'),
    ('online', 'Pay  Online')
]

class  Billing_Details(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email_address = models.EmailField(max_length=254,default="No Data")
    address_01 = models.CharField(max_length=100,default="No Data")
    address_02 = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=50,default="No Data")
    city = models.CharField(max_length=50,null=True,blank=True,choices=CITIES)
    postal_code = models.IntegerField(default=1)
    order_notes = models.TextField(default="No Data",null=True,blank=True)
    total_amt = models.IntegerField(default=1)
    payement_method = models.CharField(max_length=50,default="No Data",choices=PAYEMENT_TYPE)
    anonmyous_user_id = models.OneToOneField(Anonmyous_User, on_delete=models.DO_NOTHING,null=True,blank=True,unique=True,limit_choices_to={'active_status': '1'})
    is_paid = models.BooleanField(default=False,null=True,blank=True)
    
    class Meta:
        verbose_name = 'Billing Detail'
        verbose_name_plural = 'Billing Details'
    
    def __str__(self):
        return str(self.anonmyous_user_id)

class Payement_Details(models.Model):
    razorpay_payment_id = models.CharField(max_length=100)
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_signature = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Payment Detail"
    
