# Generated by Django 4.0.4 on 2022-08-28 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_cart_extra_productquantity_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.cart'),
        ),
    ]
