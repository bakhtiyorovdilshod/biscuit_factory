# Generated by Django 3.1.1 on 2020-11-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_product', '0003_auto_20201121_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='currency',
            field=models.CharField(choices=[('SOM', 1), ('USD', 2)], max_length=10),
        ),
    ]
