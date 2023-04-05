# Generated by Django 3.2.6 on 2021-08-12 08:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
