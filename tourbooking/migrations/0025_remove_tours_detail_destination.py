# Generated by Django 3.2.6 on 2021-11-08 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0024_auto_20211108_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tours',
            name='detail_destination',
        ),
    ]
