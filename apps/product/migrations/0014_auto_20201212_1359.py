# Generated by Django 3.1.1 on 2020-12-12 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_product', '0013_auto_20201212_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproductlog',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_product.product'),
        ),
    ]