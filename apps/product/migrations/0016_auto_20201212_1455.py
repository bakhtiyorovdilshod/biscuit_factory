# Generated by Django 3.1.1 on 2020-12-12 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_product', '0015_productpricelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addmanufacturedproduct',
            name='price',
        ),
        migrations.RemoveField(
            model_name='addmanufacturedproduct',
            name='total_price',
        ),
    ]
