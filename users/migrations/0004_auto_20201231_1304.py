# Generated by Django 2.2.17 on 2020-12-31 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_first_name_test_length"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="first_name_test_length2",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="first_name_test_length3",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
