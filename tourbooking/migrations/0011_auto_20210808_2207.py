# Generated by Django 3.2.6 on 2021-08-08 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0010_auto_20210808_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Provincial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='category_service',
            new_name='category_hotel',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='time',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='time_close',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='time_open',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='traffic',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='time_close',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='time_open',
        ),
        migrations.AddField(
            model_name='hotel',
            name='star',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tourbooking.district')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='provincial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tourbooking.provincial'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tourbooking.district'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='provincial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tourbooking.provincial'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tourbooking.ward'),
        ),
    ]