# Generated by Django 4.2.7 on 2023-11-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rate_profile_rates'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
