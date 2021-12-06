# Generated by Django 3.2.6 on 2021-11-12 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0025_remove_tours_detail_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/%Y/%m')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tourbooking.tours')),
            ],
        ),
    ]