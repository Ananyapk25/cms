# Generated by Django 3.2.5 on 2021-07-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_prefix'),
    ]

    operations = [
        migrations.AddField(
            model_name='prefix',
            name='auth',
            field=models.SlugField(default='rr', verbose_name='Auth'),
            preserve_default=False,
        ),
    ]