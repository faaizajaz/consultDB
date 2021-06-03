from django.contrib.postgres.operations import TrigramExtension

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_auto_20210602_0634'),
    ]

    operations = [
        TrigramExtension(),
    ]