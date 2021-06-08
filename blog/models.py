from django.db import models

# Create your models here.

class blogs(models.Model):
	heading = models.CharField(max_length=50)
	content= models.TextField()
	img = models.ImageField(models.ImageField(
		upload_to='uploads/blog'))
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name="Blog"
		verbose_name_plural="Blogs"

