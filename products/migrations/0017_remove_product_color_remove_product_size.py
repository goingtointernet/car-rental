# Generated by Django 4.0.4 on 2023-08-19 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_product_shipping_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
