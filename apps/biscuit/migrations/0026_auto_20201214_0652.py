# Generated by Django 3.1.1 on 2020-12-14 06:52

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0025_auto_20201213_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addunfitbiscuitlog',
            name='quantity',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='buyingbiscuit',
            name='quantity',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='buyingbiscuit',
            name='total_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='buyingbiscuitlog',
            name='quantity',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='buyingbiscuitlog',
            name='total_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='producebiscuit',
            name='quantity',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='producebiscuit',
            name='total_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='producebiscuitlog',
            name='quantity',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='producebiscuitlog',
            name='total_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='unfitbiscuit',
            name='quantity',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='unfitbiscuit',
            name='total_price',
            field=models.DecimalField(decimal_places=4, default=Decimal('0'), max_digits=10),
        ),
    ]
