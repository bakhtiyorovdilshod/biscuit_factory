# Generated by Django 3.1.1 on 2020-12-12 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0012_remove_producebiscuit_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='biscuit',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]