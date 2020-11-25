# Generated by Django 3.1.1 on 2020-11-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_supplier', '0002_auto_20201124_0542'),
        ('apps_product', '0007_auto_20201122_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_supplier.supplier'),
        ),
    ]