# Generated by Django 4.0.4 on 2022-05-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_quantity',
            field=models.ManyToManyField(blank=True, to='order.productquantity'),
        ),
    ]
