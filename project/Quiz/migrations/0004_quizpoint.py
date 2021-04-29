# Generated by Django 3.2 on 2021-04-29 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_quizattempt'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.BigIntegerField(default=0)),
                ('quizattempt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.quizattempt')),
            ],
        ),
    ]
