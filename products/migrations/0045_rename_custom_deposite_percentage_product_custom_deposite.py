# Generated by Django 5.0.1 on 2024-07-17 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0044_customdiscount_valid_cars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='custom_deposite_percentage',
            new_name='custom_deposite',
        ),
    ]
