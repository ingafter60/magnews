# Generated by Django 2.2.5 on 2020-01-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_main_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='twt',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='ytb',
            field=models.TextField(default='-'),
        ),
    ]
