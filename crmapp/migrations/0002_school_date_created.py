# Generated by Django 4.2.4 on 2023-08-11 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
