from django.db import models

# Create your models here.
class User(models.Model):
	full_name= models.CharField(max_length=100)
	organisation_type= models.CharField(max_length=10)
	organisation_name= models.CharField(max_length=20)
	designation= models.CharField(max_length=20)
	pin_code= models.CharField(max_length=6, default="143001")
	email= models.EmailField( max_length = 254 )
	phone_number= models.CharField(max_length=10)
	city= models.CharField(max_length=20)
	password= models.CharField(default=None,max_length=50)
	valid= models.BooleanField(default=False)



