# Generated by Django 3.2.6 on 2021-12-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0036_news_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_add',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_update',
            field=models.DateField(auto_now=True),
        ),
    ]
