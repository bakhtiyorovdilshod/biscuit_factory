# Generated by Django 3.1.1 on 2020-12-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0021_buyingbiscuit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyingbiscuit',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]