# Generated by Django 3.1.1 on 2020-12-13 15:00

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apps_client', '0002_auto_20201213_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 12, 13, 15, 0, 51, 379584, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='inn',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='m_f_o',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number is error', regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='client',
            name='x_p',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]