# Generated by Django 3.2.6 on 2021-08-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0017_auto_20210814_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AddField(
            model_name='tours',
            name='price_children',
            field=models.FloatField(default=0),
        ),
    ]
