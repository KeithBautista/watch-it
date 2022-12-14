# Generated by Django 3.2.16 on 2022-11-28 02:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchit', '0013_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dq4hocok1/image/upload/v1669434603/defaultProfilePic_fepkbo.webp', max_length=255, verbose_name='image'),
        ),
    ]
