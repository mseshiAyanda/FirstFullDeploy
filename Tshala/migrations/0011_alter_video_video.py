# Generated by Django 4.0.4 on 2022-05-08 01:38

import Tshala.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tshala', '0010_auto_20210131_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, upload_to='video/%y', validators=[Tshala.validators.file_size]),
        ),
    ]
