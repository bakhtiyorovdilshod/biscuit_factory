# Generated by Django 3.1.1 on 2020-12-01 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_expense', '0002_quantityexpense'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantityexpense',
            name='currency',
            field=models.CharField(default="So'm", max_length=10),
        ),
    ]