# Generated by Django 3.1.1 on 2020-12-04 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0005_auto_20201204_1625'),
        ('apps_warehouse', '0007_warehousemanufacturedproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='WareHouseUnfitBiscuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('unit_of_measurement', models.CharField(blank=True, default='kg', max_length=200, null=True)),
                ('total_price', models.IntegerField(default=0)),
                ('currency', models.CharField(default="So'm", max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('biscuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit')),
            ],
        ),
    ]
