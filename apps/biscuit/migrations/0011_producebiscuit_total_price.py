# Generated by Django 3.1.1 on 2020-12-12 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0010_auto_20201211_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='producebiscuit',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]