# Generated by Django 3.1.1 on 2020-12-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0005_auto_20201204_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unfitbiscuit',
            name='status',
            field=models.CharField(choices=[('recyclable', 'recyclable'), ('unrecyclable', 'unrecyclable')], max_length=100),
        ),
    ]
