# Generated by Django 3.0.5 on 2020-06-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_auto_20200614_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='admin_photos/'),
            preserve_default=False,
        ),
    ]
