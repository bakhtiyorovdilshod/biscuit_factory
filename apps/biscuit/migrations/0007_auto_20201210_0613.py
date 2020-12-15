# Generated by Django 3.1.1 on 2020-12-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0006_auto_20201204_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producebiscuit',
            name='date',
        ),
        migrations.AddField(
            model_name='producebiscuit',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='producebiscuit',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]