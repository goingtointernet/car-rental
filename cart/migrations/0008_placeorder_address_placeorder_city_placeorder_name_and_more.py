# Generated by Django 4.0.4 on 2022-07-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_placeorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeorder',
            name='address',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AddField(
            model_name='placeorder',
            name='city',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='placeorder',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='placeorder',
            name='phone',
            field=models.IntegerField(default=123456789),
        ),
        migrations.AddField(
            model_name='placeorder',
            name='state',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='placeorder',
            name='zip_code',
            field=models.IntegerField(default='123'),
        ),
    ]
