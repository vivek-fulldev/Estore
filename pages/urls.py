from django.urls import path
from .views import *

urlpatterns =[
	path("contact",contact),
	path("page/<slug:data>",Pages),
]
