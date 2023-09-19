# Generated by Django 4.0.4 on 2022-06-11 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_alter_lecture_resourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='course',
        ),
        migrations.AddField(
            model_name='lecture',
            name='coursesection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.coursesection'),
        ),
    ]