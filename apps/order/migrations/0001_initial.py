# Generated by Django 3.1.1 on 2021-01-29 17:10

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps_biscuit', '0035_remove_producebiscuit_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('comment', models.TextField()),
                ('status', models.CharField(blank=True, choices=[('pending', 'pending'), ('completed', 'completed')], default='unpaid', max_length=50, null=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('biscuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit')),
            ],
        ),
    ]