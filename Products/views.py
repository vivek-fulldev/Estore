import datetime
import string
import random  # define the random module
import razorpay

from django.shortcuts import render
from .models import Products, Product_Image, Coupon_Management, Order_Management
from user_profiles.models import Anonmyous_User
from billing_details.models import Billing_Details
from django.http.response import JsonResponse, HttpResponse
from datetime import timedelta, datetime
from .forms import Billing_DetailsForm
# Create your views here.


def index(request):
	data = Products.objects.all()
	print("ttttttttttttttttttttttttttttttttttttttttttt",type(data))
	all_data = []
	for i in data:
		all_dic = {}
		all_dic['product_name'] = i.product_name
		all_dic['price'] = i.price
		all_dic['cutting_price'] = i.cutting_price
		all_dic['is_featured'] = i.is_featured
		all_dic['product_image'] = i.product_image
		all_dic['discount'] = i.discount
		all_dic['id'] = i.id
		a = i.created_at + timedelta(days=10)
		date = a.strftime("%m/%d/%Y")
		now = datetime.now()
		current_date = now.strftime("%m/%d/%Y")
		if date > current_date:
			all_dic['new_product'] = True
		all_data.append(all_dic)
	return render(request, 'index.html', {"products_data": all_data})


def product_details(request, pk):
	i = Products.objects.get(id=pk)
	print("ttttttttttttttttttttttttttttttttttttttttttt",type(i))
	size = str(i.size).split(',')
	all_dic = {}
	all_dic['product_name'] = i.product_name
	all_dic['price'] = i.price
	all_dic['cutting_price'] = i.cutting_price
	all_dic['is_featured'] = i.is_featured
	all_dic['is_discountable'] = i.is_discountable
	all_dic['product_image'] = i.product_image
	all_dic['discount'] = i.discount
	all_dic['id'] = i.id
	all_dic['description'] = i.description
	all_dic['category'] = i.category
	all_dic['size'] = size

	img = Product_Image.objects.filter(product_name_id=pk)
	image = []
	for i in img:
		all_img = {}
		all_img['image'] = i.product_image
		image.append(all_img)
	return render(request, 'product.html', {"product_data": all_dic, "image": image})


def Coupon(request):
	if request.method == 'POST':
		coupon_code = request.POST.get('coupon_code')
		code = Coupon_Management.objects.filter(coupon_code=coupon_code)
		if code:
			price = code[0].product.price
			discount = code[0].product.discount
			total_amt = price - discount/100 * price
			return JsonResponse({'success': True, "amount": total_amt})
		else:
			return JsonResponse({"success": False, "msg": "Coupon Code Invalid !"})


def Checkout(request, data):
	global total
	total = 0
	user = Anonmyous_User.objects.filter(user_id=data)
	if user.exists():
		user = Anonmyous_User.objects.get(user_id=data)
		products = Order_Management.objects.filter(anonmyous_user_id=user)
		sub_total = 0
		for product in products:
			sub_total += product.total_amt
		gst = round((9/100) * sub_total)
		total = round((2*gst) + sub_total)
	if request.method == 'GET':
		return render(request, 'checkout.html', {"product_data": products, "sub_total": sub_total, "gst": gst, "total": total})
	if request.method == 'POST':
		q = request.POST.copy()
		q.update({'total_amt': total})
		if Anonmyous_User.objects.filter(user_id=data):
			user = Anonmyous_User.objects.get(user_id=data)
			q.update({'anonmyous_user_id': user})
		form = Billing_DetailsForm(q)
		if form.is_valid():
			form.save()
			return JsonResponse({"success": True})
		else:
			return JsonResponse({"success": False, "error": form.errors})
	return render(request, 'checkout.html')


def Pay(request, data):
	if Anonmyous_User.objects.filter(user_id=data,active_status=True):
		user_id = Anonmyous_User.objects.get(user_id=data)
		bill = Billing_Details.objects.get(anonmyous_user_id=user_id)
		return render(request, 'pay.html', {"name": bill.first_name + bill.last_name, "amount": bill.total_amt*100, "email": bill.email_address, "user_id": data})
	else:
		return render(request,'404.html')


def Order(request):
	if request.method == 'POST':
		product_id = request.POST['product_id']
		quantity = int(request.POST['quantity'])
		size = request.POST['size']
		total_amt = float(request.POST['total_amt'])
		if Products.objects.filter(id=product_id).exists() == False:
			return JsonResponse({"success": False})
		if quantity > 10 or quantity < 0:
			return JsonResponse({"success": False})
		pd = Products.objects.get(id=product_id)
		d = pd.discount
		p = pd.price
		s = p - (d/100)*p
		min_amt = quantity * s
		if total_amt < min_amt:
			return JsonResponse({"success": False})
		a = Products.objects.get(id=product_id)
		if str(request.POST['anonmyous_user_id']) == "null":
			S = 20
			anonmyous_user_id = ''.join(random.choices(
				string.ascii_lowercase + string.digits, k=S))
			user = Anonmyous_User.objects.create(user_id=anonmyous_user_id)
			user.save()
			user = Anonmyous_User.objects.get(user_id=anonmyous_user_id)
			order = Order_Management.objects.create(
				product_id=a, quantity=quantity, size=size, total_amt=total_amt, anonmyous_user_id=user)
			order.save()
			return JsonResponse({"success": True, "anonmyous_user_id": anonmyous_user_id})
		user = Anonmyous_User.objects.filter(
			user_id=request.POST['anonmyous_user_id'])
		if user.exists():
			user = Anonmyous_User.objects.get(
				user_id=request.POST['anonmyous_user_id'])
			order = Order_Management.objects.create(
				product_id=a, quantity=quantity, size=size, total_amt=total_amt, anonmyous_user_id=user)
			order.save()
			return JsonResponse({"success": True, "anonmyous_user_id": False})
		return JsonResponse({"success": False})


def Cart(request, data):
	if request.method == 'GET':
		user = Anonmyous_User.objects.filter(user_id=data)
		if user.exists():
			user = Anonmyous_User.objects.get(user_id=data)
			products = Order_Management.objects.filter(anonmyous_user_id=user)
	return render(request, "cart.html", {"product_data": products})


def Confirmation(request,data):
	user = Anonmyous_User.objects.filter(user_id=data,active_status=True) 
	if user:
		client = razorpay.Client(
			auth=('rzp_test_dcBBiMbxp0f5NY', 'vpqrptECJa0AuE2Bfhquh8R6'))
		user_id = Anonmyous_User.objects.get(user_id=data)
		bill = Billing_Details.objects.filter(anonmyous_user_id=user_id)
		bill.update(is_paid=True)
		bill = Billing_Details.objects.get(anonmyous_user_id=user_id)
		products = Order_Management.objects.filter(anonmyous_user_id=user_id)
		sub_total = 0
		for product in products:
			sub_total += product.total_amt
		gst = round((9/100) * sub_total)
		total = round((2*gst) + sub_total)
		user.update(active_status = False)	
		return render(request, 'confirmation.html',{"bill_data":bill,"product_data": products, "sub_total": sub_total, "gst": gst, "total": total})	
	else:
		return render(request,'404.html')

