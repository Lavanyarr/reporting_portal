# Generated by Django 2.2.1 on 2020-07-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting_portal', '0006_observation_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='reported_on',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]