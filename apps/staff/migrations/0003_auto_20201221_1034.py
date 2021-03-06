# Generated by Django 3.1.1 on 2020-12-21 05:34

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_user', '0001_initial'),
        ('apps_staff', '0002_auto_20201219_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffBiscuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biscuit_quantity', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('status', models.CharField(choices=[('un_calculate', 'un_calculate'), ('calculated', 'calculated')], default='un_calculate', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_user.account')),
            ],
        ),
        migrations.DeleteModel(
            name='SalaryPercentage',
        ),
    ]
