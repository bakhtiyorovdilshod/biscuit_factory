# Generated by Django 3.1.1 on 2020-12-13 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_product', '0018_auto_20201212_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproduct',
            name='status',
            field=models.CharField(blank=True, choices=[('unpaid', 'unpaid'), ('paid', 'paid')], default='unpaid', max_length=50, null=True),
        ),
    ]