# Generated by Django 2.2.5 on 2020-01-19 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200120_0002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='footer_link',
            new_name='setname',
        ),
        migrations.RenameField(
            model_name='main',
            old_name='set_name',
            new_name='website',
        ),
    ]