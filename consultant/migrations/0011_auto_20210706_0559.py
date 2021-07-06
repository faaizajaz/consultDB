# Generated by Django 3.1.4 on 2021-07-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expertise', '0001_initial'),
        ('consultant', '0010_auto_20210618_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='cv_file_1',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='CV slot 1'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='cv_file_2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='CV slot 2'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='cv_file_3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='CV slot 3'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='practice_areas',
            field=models.ManyToManyField(to='expertise.PracticeArea'),
        ),
    ]