# Generated by Django 4.0.4 on 2022-07-04 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_category_category_img_alter_color_color_img'),
        ('cart', '0004_alter_cart_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.color'),
        ),
    ]
