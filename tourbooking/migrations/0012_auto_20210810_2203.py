# Generated by Django 3.2.6 on 2021-08-10 15:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0011_auto_20210808_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='star',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
