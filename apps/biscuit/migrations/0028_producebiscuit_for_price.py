# Generated by Django 3.1.1 on 2020-12-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0027_auto_20201214_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='producebiscuit',
            name='for_price',
            field=models.CharField(choices=[('un_calculate', 'un_calculate'), ('calculated', 'calculated')], default='un_calculate', max_length=50),
        ),
    ]
