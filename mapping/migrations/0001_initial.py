# Generated by Django 3.1 on 2020-08-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # migrations.RunSQL("CREATE EXTENSION IF NOT EXISTS hstore"),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('MappingID', models.IntegerField(primary_key=True, serialize=False)),
                ('UserID', models.IntegerField(null=True)),
                ('MappingFor', models.TextField(null=True)),
                ('CreatedOn', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]