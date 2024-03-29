# Generated by Django 3.1.4 on 2020-12-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_auto_20201206_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='contracted_rate',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rate at which consultant was contracted'),
        ),
        migrations.AddField(
            model_name='rating',
            name='date_of_engagement',
            field=models.DateField(blank=True, null=True, verbose_name='The date of engagement'),
        ),
        migrations.AddField(
            model_name='rating',
            name='days_worked',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of days contracted'),
        ),
    ]
