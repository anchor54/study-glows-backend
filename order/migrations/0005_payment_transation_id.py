# Generated by Django 4.0.4 on 2022-06-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_productquantity_testseries_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='transation_id',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
