# Generated by Django 4.2.6 on 2024-01-09 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_remove_product_how_use_remove_product_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
