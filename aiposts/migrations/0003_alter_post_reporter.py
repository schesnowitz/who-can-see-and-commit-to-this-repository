# Generated by Django 4.2 on 2023-05-07 22:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aiposts", "0002_post_reporter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="reporter",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]