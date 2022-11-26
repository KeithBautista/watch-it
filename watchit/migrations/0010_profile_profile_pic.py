# Generated by Django 3.2.16 on 2022-11-26 02:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchit', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='default', max_length=255, verbose_name='profile'),
        ),
    ]
