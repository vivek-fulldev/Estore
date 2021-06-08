from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product/<int:pk>', product_details),
    path('coupon', Coupon),
    path('checkout/<slug:data>',Checkout),
    path('order',Order),
    path('cart/<slug:data>',Cart),
    path('pay/<slug:data>',Pay),
    path('confirmation/<slug:data>',Confirmation),
    path('',index,name="index"),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)