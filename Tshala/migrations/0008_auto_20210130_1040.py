# Generated by Django 3.1.5 on 2021-01-30 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tshala', '0007_video_information'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='information',
            new_name='add',
        ),
    ]
