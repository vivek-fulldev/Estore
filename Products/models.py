from django.db import models
from django.utils import timezone
from user_profiles.models import Anonmyous_User
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError


# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.category_name


size_choices = (
	('XS', 'Xtra Small Size'),
	('S', 'Small Size'),
	('M', 'Medium Size'),
	('L', 'Large'),
	('XL', 'Xtra Size Size')
)


def is_discountable(value):
	is_discountable.values = value

def discount(value):
	discount.values = value
	if is_discountable.values and value <= 0 or value > 50:
		raise ValidationError("Please Enter Valid Value in Discount field")
	if is_discountable.values == False and value != 0:
		raise ValidationError("Please Enter Zero  in Discount field")


class Products(models.Model):
	product_name = models.CharField(max_length=100)
	price = models.IntegerField()
	cutting_price = models.IntegerField()
	is_featured = models.BooleanField()
	is_discountable = models.BooleanField(validators=[is_discountable])
	discount = models.IntegerField(default=0,
		 validators=[discount],verbose_name="Discount Percentage")
	product_image = models.ImageField(
		upload_to='uploads/product', default="No Image")
	description = models.TextField(blank=True, null=True)
	category = models.OneToOneField(Category, on_delete=models.CASCADE)
	size = MultiSelectField(choices=size_choices, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def __str__(self):
		return self.product_name


class Product_Image(models.Model):
	product_name = models.ForeignKey(
		Products, on_delete=models.CASCADE, related_name="images")
	product_image = models.ImageField(
		upload_to='uploads/product', default="No Image")

	class Meta:
		verbose_name = "Product Image"
		verbose_name_plural = "Product Images"

	def __str__(self):
		return str(self.product_name)

class Coupon_Management(models.Model):
	coupon_code = models.CharField(max_length=50)
	product = models.ForeignKey(Products,on_delete=models.DO_NOTHING,default=1)
	
	class Meta:
		verbose_name ="Coupon"
		verbose_name_plural="Coupons"

	def __str__(self):
		return self.coupon_code

class Order_Management(models.Model):
	product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
	quantity = models.IntegerField()
	size = models.CharField(max_length=50, null=True,blank=True)
	total_amt = models.IntegerField()
	anonmyous_user_id = models.ForeignKey(Anonmyous_User, on_delete=models.CASCADE,null=True,blank=True,limit_choices_to={'active_status': '1'}) 

	class Meta:
		verbose_name = 'Order Product'

	def __str__(self):
		return str(self.product_id)

	