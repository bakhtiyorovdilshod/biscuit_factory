# Generated by Django 3.1.1 on 2020-12-12 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0011_producebiscuit_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producebiscuit',
            name='total_price',
        ),
    ]
