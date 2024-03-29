# Generated by Django 4.0.4 on 2024-02-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_homesectiontwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatreonImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='patreon_logos')),
            ],
        ),
        migrations.DeleteModel(
            name='HomeSectionOne',
        ),
        migrations.AddField(
            model_name='sitedata',
            name='brand',
            field=models.ManyToManyField(blank=True, null=True, to='home.patreonimage'),
        ),
    ]
