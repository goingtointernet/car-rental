# Generated by Django 5.0.1 on 2024-03-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0023_booking_insurance_amount_cart_insurance_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='dropoff_time',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pickup_time',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='dropoff_time',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='pickup_time',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
    ]