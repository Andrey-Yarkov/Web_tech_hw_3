# Generated by Django 4.2.7 on 2023-11-14 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_answer_is_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='creation_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
