# Generated by Django 3.1.1 on 2020-12-13 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_product', '0019_addproduct_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addproduct',
            name='status',
        ),
    ]
