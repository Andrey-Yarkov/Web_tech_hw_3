# Generated by Django 4.2.7 on 2023-11-14 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_question_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answers_count',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='questions', to='app.tag'),
        ),
    ]
