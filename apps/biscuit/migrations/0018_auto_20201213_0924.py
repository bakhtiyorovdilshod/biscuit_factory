# Generated by Django 3.1.1 on 2020-12-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_biscuit', '0017_auto_20201213_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='addunfitbiscuitlog',
            name='unfit_biscuit_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='AddUnFitBiscuit',
        ),
    ]
