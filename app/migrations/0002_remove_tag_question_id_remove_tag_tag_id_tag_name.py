# Generated by Django 4.2.7 on 2023-11-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_id',
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
