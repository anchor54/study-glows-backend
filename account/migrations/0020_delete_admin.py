# Generated by Django 4.2.5 on 2023-09-19 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_rename_user_admin_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
    ]