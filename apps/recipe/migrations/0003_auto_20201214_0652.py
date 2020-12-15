# Generated by Django 3.1.1 on 2020-12-14 06:52

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_recipe', '0002_manufacturedproductrecipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biscuitrecipe',
            name='value',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='manufacturedproductrecipe',
            name='value',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
    ]