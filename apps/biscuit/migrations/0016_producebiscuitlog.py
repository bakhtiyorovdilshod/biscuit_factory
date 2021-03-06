# Generated by Django 3.1.1 on 2020-12-12 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_user', '0001_initial'),
        ('apps_biscuit', '0015_auto_20201212_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduceBiscuitLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('currency', models.CharField(blank=True, default="so'm", max_length=200, null=True)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(blank=True, choices=[('completed', 'completed'), ('pending', 'pending')], default='pending', max_length=200, null=True)),
                ('produce_biscuit_id', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('biscuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apps_user.account')),
            ],
        ),
    ]
