# Generated by Django 5.0.1 on 2024-06-27 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_product_discount_product_seven_day_book_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seven_day_book_discount',
        ),
    ]
