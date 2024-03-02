# Generated by Django 5.0.1 on 2024-03-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_product_damage_coverage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_timing',
            field=models.CharField(choices=[('1:00 AM', '1:00 AM'), ('2:00 AM', '2:00 AM'), ('3:00 AM', '3:00 AM'), ('4:00 AM', '4:00 AM'), ('5:00 AM', '5:00 AM'), ('6:00 AM', '6:00 AM'), ('7:00 AM', '7:00 AM'), ('8:00 AM', '8:00 AM'), ('9:00 AM', '9:00 AM'), ('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'), ('12:00 AM', '12:00 AM'), ('1:00 PM', '1:00 PM'), ('2:00 PM', '2:00 PM'), ('3:00 PM', '3:00 PM'), ('4:00 PM', '4:00 PM'), ('5:00 PM', '5:00 PM'), ('6:00 PM', '6:00 PM'), ('7:00 PM', '7:00 PM'), ('8:00 PM', '8:00 PM'), ('9:00 PM', '9:00 PM'), ('10:00 PM', '10:00 PM'), ('11:00 PM', '11:00 PM'), ('12:00 PM', '12:00 PM')], default='', max_length=255),
        ),
    ]
