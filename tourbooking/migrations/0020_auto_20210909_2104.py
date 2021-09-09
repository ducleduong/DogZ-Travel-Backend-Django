# Generated by Django 3.2.6 on 2021-09-09 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0019_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingtour',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'news')},
        ),
        migrations.AlterUniqueTogether(
            name='ratingtour',
            unique_together={('user', 'tour')},
        ),
    ]
