# Generated by Django 5.0.1 on 2024-04-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0024_alter_booking_dropoff_time_alter_booking_pickup_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='coupon',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='discount_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
