from django import forms  
from billing_details.models import Billing_Details  
  
class Billing_DetailsForm(forms.ModelForm):  
    class Meta:  
        model = Billing_Details  
        fields = "__all__"  