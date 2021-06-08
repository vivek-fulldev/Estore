from django.db import models

# Create your models here.


class contact(models.Model):
	msg = models.TextField(max_length=350)
	name= models.CharField(max_length=50)
	email_address = models.EmailField()
	subject = models.CharField(max_length=100)

	class Meta:
		verbose_name='Contact'

	def __str__(self):
		return self.email_address


class pages(models.Model):
	url= models.CharField(max_length=20,unique=True)
	heading = models.CharField(max_length=10)
	is_active=models.BooleanField(default=True)

	class Meta:
		verbose_name='Page'

	def __str__(self):
		return self.url

class content(models.Model):
	heading= models.CharField(max_length=50,null=True,blank=True)
	subcontent = models.TextField(null=True,blank=True)
	page_id = models.ForeignKey(pages, on_delete=models.CASCADE,limit_choices_to={'is_active':'1'})
	class Meta:
		verbose_name='Content'

	def __str__(self):
		return str(self.page_id)

