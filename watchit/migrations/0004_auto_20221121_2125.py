# Generated by Django 3.2.16 on 2022-11-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchit', '0003_auto_20221120_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Action', max_length=255),
        ),
    ]