# Generated by Django 3.1.1 on 2020-11-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_warehouse', '0004_warehouseproduct_average_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseproduct',
            name='currency',
            field=models.CharField(default="So'm", max_length=10),
        ),
    ]
