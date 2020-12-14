# Generated by Django 3.1.1 on 2020-12-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0023_auto_20201213_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producebiscuit',
            name='status',
            field=models.CharField(blank=True, choices=[('unpaid', 'unpaid'), ('paid', 'paid')], default='unpaid', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='producebiscuitlog',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
