# Generated by Django 4.0.4 on 2022-06-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color_img',
            field=models.ImageField(upload_to='static/images/product/color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(upload_to='static/images/product'),
        ),
    ]
