from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth.models import User
# Create your views here.
def index(request):
	if request.method == 'POST':
		full_name = request.POST['full_name']
		organisation_type = request.POST['organisation_type']
		organisation_name = request.POST['organisation_name']
		designation = request.POST['designation']
		pin_code = request.POST['pin_code']
		email = request.POST['email']
		phone_number = request.POST['phone_number']
		city = request.POST['city']
		password=User.objects.make_random_password()

		user = User(full_name=full_name,organisation_type=organisation_type,organisation_name=organisation_name,designation=designation,pin_code=pin_code,email=email,phone_number=phone_number,city=city,password=password)
		user.save()
		print('user created')
		return render(request,'signin.html')


	else:
		return render(request,'index.html')
		
























def signin(request):
	return render(request,'signin.html')
def login(request):
	return render(request,'login.html')
def dashboard(request):
	return render(request,'dashboard.html')
def mandates(request):
	return render(request,'mandates.html')
def upload(request):
	return render(request,'upload.html')
def badrecords(request):
	return render(request,'badrecords.html')
def manageteam(request):
	return render(request,'manageteam.html')
def contacts(request):
	return render(request,'contacts.html')