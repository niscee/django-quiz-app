# Generated by Django 3.2 on 2021-04-29 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_quizpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizpoint',
            name='percentage',
            field=models.BigIntegerField(default=0),
        ),
    ]
