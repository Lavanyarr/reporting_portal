# Generated by Django 2.2.1 on 2020-07-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting_portal', '0005_auto_20200723_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='assigned_to',
            field=models.IntegerField(null=True),
        ),
    ]
