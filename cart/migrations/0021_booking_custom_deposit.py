# Generated by Django 5.0.1 on 2024-03-01 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0020_rename_product_cart_car_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='custom_deposit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]