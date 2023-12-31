# Generated by Django 4.0.4 on 2022-05-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ('-created_at', 'score')},
        ),
        migrations.AddField(
            model_name='instructor',
            name='score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
