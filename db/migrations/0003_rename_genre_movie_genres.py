# Generated by Django 4.0.2 on 2024-01-27 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_cinemahall_movie_moviesession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='genres',
        ),
    ]
