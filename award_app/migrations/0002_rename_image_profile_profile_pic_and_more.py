# Generated by Django 4.0.3 on 2022-03-13 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_pic',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_title',
            new_name='title',
        ),
    ]
