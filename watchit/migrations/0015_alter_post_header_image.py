# Generated by Django 3.2.16 on 2022-11-28 02:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchit', '0014_alter_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dq4hocok1/image/upload/v1669602662/imageNotAvailable_uklilq.webp', max_length=255, verbose_name='image'),
        ),
    ]
