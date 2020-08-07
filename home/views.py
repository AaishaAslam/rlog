from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
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
	
