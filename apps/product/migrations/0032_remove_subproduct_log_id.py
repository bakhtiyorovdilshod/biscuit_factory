# Generated by Django 3.1.1 on 2021-01-07 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_product', '0031_auto_20201225_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subproduct',
            name='log_id',
        ),
    ]
