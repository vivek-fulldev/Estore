from django import forms
from .models import contact
  
class contactForm(forms.ModelForm):  
    class Meta:  
        model = contact  
        fields = "__all__"  
