# Generated by Django 4.0.4 on 2022-07-07 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_cart_color'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlaceOrder',
        ),
    ]
