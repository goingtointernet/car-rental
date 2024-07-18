# Generated by Django 5.0.1 on 2024-07-18 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0046_rename_pro_tips_product_why_choose_this'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features_heading',
            field=models.CharField(default='Features', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='heighlights_heading',
            field=models.CharField(default='Highlights', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='instructions_heading',
            field=models.CharField(default='instructions', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='why_choose_this_heading',
            field=models.CharField(default='Why Choose This', max_length=500),
        ),
    ]
