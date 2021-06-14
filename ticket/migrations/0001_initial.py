# Generated by Django 3.1.4 on 2021-06-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opened_by', models.CharField(max_length=500, verbose_name='Your name')),
                ('description', models.TextField(max_length=500, verbose_name='Description of the issue')),
            ],
        ),
    ]
