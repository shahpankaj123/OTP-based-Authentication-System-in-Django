# Generated by Django 4.2.1 on 2023-09-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_is_verified_profile_verifiedid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='otp',
            field=models.IntegerField(default=122),
            preserve_default=False,
        ),
    ]
