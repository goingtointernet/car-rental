# Generated by Django 4.0.4 on 2022-07-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_permalink_product_permalink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(upload_to='product_img'),
        ),
    ]
