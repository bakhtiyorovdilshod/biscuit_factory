# Generated by Django 3.1.1 on 2020-12-12 13:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apps_product', '0012_addproductlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproductlog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 12, 12, 13, 56, 45, 511234, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addproductlog',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
