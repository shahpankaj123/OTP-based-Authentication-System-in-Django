# Generated by Django 4.2.1 on 2023-09-23 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_verified',
            new_name='verifiedid',
        ),
    ]
