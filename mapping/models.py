from django.db import models
from django.contrib.postgres.operations import HStoreExtension

class Migration(migrations.Migration):
    operations = [
        HStoreExtension(),
    ]

# Create your models here.
class Mapping(models.Model):
    MappingID = models.IntegerField(primary_key = True)
    UserID = models.IntegerField()
    MappingFor = models.CharField()
    CreatedOn = models.DateField(auto_now_add = True)
    Mappings = HStoreField()
