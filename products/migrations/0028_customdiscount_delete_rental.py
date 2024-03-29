# Generated by Django 4.0.4 on 2024-02-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_rental'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount_valid_days', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
    ]
