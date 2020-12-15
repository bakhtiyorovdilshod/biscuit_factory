# Generated by Django 3.1.1 on 2020-12-14 10:40

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_product', '0022_auto_20201214_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproductlog',
            name='price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='addproductlog',
            name='quantity',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='addproductlog',
            name='total_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=20),
        ),
    ]
