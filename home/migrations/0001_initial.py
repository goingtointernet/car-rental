# Generated by Django 4.0.4 on 2022-06-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=160)),
                ('phone', models.IntegerField(default=123456789)),
                ('facebook', models.CharField(blank=True, default='', max_length=160, null=True)),
                ('instagram', models.CharField(blank=True, default='', max_length=160, null=True)),
                ('twitter', models.CharField(blank=True, default='', max_length=160, null=True)),
                ('youtube', models.CharField(blank=True, default='', max_length=160, null=True)),
                ('address', models.CharField(default='', max_length=260)),
                ('made_by', models.CharField(default='', max_length=160)),
                ('copyright', models.CharField(default='', max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='StaticPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('page_name', models.CharField(max_length=70)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=70, unique=True)),
            ],
        ),
    ]
