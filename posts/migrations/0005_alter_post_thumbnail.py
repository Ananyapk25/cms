# Generated by Django 3.2.5 on 2021-07-07 17:57

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210707_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=core.utils.upload_image_path, verbose_name='Post Thumbnail'),
        ),
    ]