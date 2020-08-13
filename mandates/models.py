from django.db import models

# Create your models here.
class Mandates(models.Model):

    JDCode = models.CharField(unique = True)
    VacancyCode = models.CharField()
    Title = models.CharField()                                                  #Job Title
    Location = models.CharField()
    HiringManager = models.CharField()
    RequisitionManager = models.CharField(blank = True)
    KeySkills = models.CharField()
    Role = models.CharField(blank = True)
    DesiredExperience = models.TextInput(blank = True)
    Education = models.CharField()
    MinExpRange = models.IntegerField()
    MaxExpRange = models.IntegerField()
    CTC = models.IntegerField(blank = True)
    NoticePeriod = models.IntegerField(blank = True)
    Status = models.CharField(max_length = 1)
    Openings = models.IntegerField()
    No_Filled = models.IntegerField()
    HiringMgrContact = models.IntegerField()
    HiringMgrEmail = models.CharField()
    RecruiterAssignedTo = models.ForeignKey('user.User')
    AssignedDate = models.DateField()
    ClientID = models.ForeignKey('records.Client')
