# Generated by Django 4.0.4 on 2022-06-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_series', '0005_testset_publish_question_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RemoveField(
            model_name='question',
            name='order',
        ),
        migrations.RemoveField(
            model_name='question',
            name='testset',
        ),
        migrations.AlterField(
            model_name='testsetcategory',
            name='publish',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
