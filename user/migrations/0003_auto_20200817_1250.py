# Generated by Django 3.1 on 2020-08-17 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200813_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserReportsTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.user'),
        ),
    ]
