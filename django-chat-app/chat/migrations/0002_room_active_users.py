# Generated by Django 4.2.5 on 2023-09-24 07:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="active_users",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
