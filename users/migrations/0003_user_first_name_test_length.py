# Generated by Django 2.2.17 on 2020-12-31 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20201231_0749"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="first_name_test_length",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
