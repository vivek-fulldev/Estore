from django.contrib import admin
from .models import blogs 
# Register your models here.

class blogsModelAdmin(admin.ModelAdmin):
	list_display = ['heading','date']



admin.site.register(blogs,blogsModelAdmin)