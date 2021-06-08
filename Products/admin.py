from django.contrib import admin
from .models import Products,Product_Image,Category,Coupon_Management,Order_Management
# Register your models here.
admin.site.register(Products)
admin.site.register(Product_Image)
admin.site.register(Category)
admin.site.register(Coupon_Management)
admin.site.register(Order_Management)
