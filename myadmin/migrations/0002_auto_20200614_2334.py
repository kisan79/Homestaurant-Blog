# Generated by Django 3.0.5 on 2020-06-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='admin_photos/'),
        ),
    ]
