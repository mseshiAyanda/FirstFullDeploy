# Generated by Django 3.1.4 on 2020-12-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tshala', '0002_auto_20201210_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
