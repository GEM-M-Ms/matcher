# Generated by Django 3.1.3 on 2020-11-14 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("matching", "0002_match_mentee_mentor_settings"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cohort",
            options={"ordering": ["-created_on"]},
        ),
        migrations.AlterModelOptions(
            name="match",
            options={"verbose_name_plural": "Matches"},
        ),
        migrations.AlterModelOptions(
            name="settings",
            options={"verbose_name_plural": "Settings"},
        ),
    ]