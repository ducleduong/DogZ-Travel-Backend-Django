# Generated by Django 3.2.6 on 2021-09-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0021_alter_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/'),
        ),
    ]