from django.shortcuts import render
from .forms import contactForm
from django.http.response import JsonResponse
from .models import pages,content
# Create your views here.


def contact(request):
	if request.method == 'POST':
		contact = contactForm(request.POST)
		if contact.is_valid():
			contact.save()
			return JsonResponse({"success":True,"msg":"We Registered your query updated you as soon as possible !"})
		else:
			return JsonResponse({"success":False,"error":contact.errors}) 
	return render(request,'contact.html')

def Pages(request,data):
	if pages.objects.filter(url=data):
		page = pages.objects.get(url=data,is_active=True)
		contents = content.objects.filter(page_id=page)
		return render(request,"pages.html",{"page_name":page,"page_data":contents})
	else:
		return render(request,"404.html") 