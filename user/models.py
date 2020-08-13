from django.db import models

# Create your models here.

class User(models.Model):
    UserID = models.IntegerField(primary_key = True)
    FullName = models.CharField()
    UserDescription = models.CharField()
    UserCompany = models.CharField()
    UserStatus = models.CharField(max_length = 1)
    UserReportsTo = models.ForeignKey('self', null = True)
    Password = models.CharField()
    CreatedOn = models.DateField(auto_now_add = True)
    Role = models.CharField()
    Designation = models.CharField()
    Phone = models.IntegerField(max_length = 10)
    EmailID = models.EmailField()
    Department = models.CharField(blank = True)
    ValidTill = models.DateField()
    UserType = models.CharField()
