# Generated by Django 3.2.6 on 2021-08-14 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0014_alter_ratingtravel_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryTravel',
            new_name='CategoryTour',
        ),
        migrations.RenameModel(
            old_name='RatingTravel',
            new_name='RatingTour',
        ),
        migrations.RenameModel(
            old_name='ReviewTravel',
            new_name='ReviewTour',
        ),
        migrations.RenameModel(
            old_name='Travel',
            new_name='Tours',
        ),
        migrations.RenameField(
            model_name='ratingtour',
            old_name='travel',
            new_name='tour',
        ),
        migrations.RenameField(
            model_name='reviewtour',
            old_name='travel',
            new_name='tour',
        ),
        migrations.RenameField(
            model_name='tours',
            old_name='category_travel',
            new_name='category_tour',
        ),
    ]
