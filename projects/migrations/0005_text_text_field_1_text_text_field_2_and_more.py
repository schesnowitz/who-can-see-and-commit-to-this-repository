# Generated by Django 4.2 on 2023-05-08 12:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_delete_aipost"),
    ]

    operations = [
        migrations.AddField(
            model_name="text",
            name="text_field_1",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="text",
            name="text_field_2",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="text",
            name="text_field_3",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="text",
            name="text_field_4",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]