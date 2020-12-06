# Generated by Django 3.1.4 on 2020-12-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(default='', verbose_name='Additional comments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='project_code',
            field=models.CharField(default='', max_length=10, verbose_name='OPM project code'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='star_rating',
            field=models.IntegerField(default=0, verbose_name='Rating from 1-5'),
        ),
    ]