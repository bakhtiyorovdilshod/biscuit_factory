# Generated by Django 3.1.1 on 2020-12-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
