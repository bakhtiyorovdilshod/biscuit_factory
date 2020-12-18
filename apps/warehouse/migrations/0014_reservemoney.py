# Generated by Django 3.1.1 on 2020-12-15 17:22

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_warehouse', '0013_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReserveMoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('percentage', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]