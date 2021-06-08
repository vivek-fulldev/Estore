from django.shortcuts import render
from .models import blogs
# Create your views here.
def all_blog(request):
	blog = blogs.objects.all()
	print("ppppppppppppp",blog[0].date)
	return render(request,'blog.html',{"blog_data":blog})