# Generated by Django 5.0.1 on 2024-06-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_customdiscount_seven_day_booking_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller_email',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='seller_name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='seller_phone',
            field=models.CharField(default='', max_length=300),
        ),
    ]
