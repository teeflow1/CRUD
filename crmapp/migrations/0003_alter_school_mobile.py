# Generated by Django 4.2.4 on 2023-08-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0002_school_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='mobile',
            field=models.CharField(max_length=14),
        ),
    ]
