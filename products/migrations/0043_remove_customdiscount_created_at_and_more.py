# Generated by Django 5.0.1 on 2024-06-27 12:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0042_product_seller_email_product_seller_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customdiscount',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customdiscount',
            name='discount_valid_days',
        ),
        migrations.RemoveField(
            model_name='customdiscount',
            name='valid_cars',
        ),
        migrations.AddField(
            model_name='customdiscount',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customdiscount',
            name='valid_from',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customdiscount',
            name='valid_to',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
