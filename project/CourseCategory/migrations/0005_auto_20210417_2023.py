# Generated by Django 3.2 on 2021-04-17 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CourseCategory', '0004_auto_20210417_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedetail',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='coursedetail',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='CourseCategory',
        ),
        migrations.DeleteModel(
            name='CourseDetail',
        ),
    ]
