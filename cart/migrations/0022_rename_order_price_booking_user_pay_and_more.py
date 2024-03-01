# Generated by Django 5.0.1 on 2024-03-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0021_booking_custom_deposit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='order_price',
            new_name='user_pay',
        ),
        migrations.AddField(
            model_name='booking',
            name='remaning_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='custom_deposit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='remaning_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
