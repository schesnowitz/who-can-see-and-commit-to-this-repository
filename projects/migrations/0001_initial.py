# Generated by Django 4.2 on 2023-04-22 05:50

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Text",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "page_text_1",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_2",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_3",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_4",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_5",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_6",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_7",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_8",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_9",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_10",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_11",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_12",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_13",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_14",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_15",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_16",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_17",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_18",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_19",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_20",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "page_text_21",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                ("facebook_url", models.URLField(blank=True, null=True)),
                ("github_url", models.URLField(blank=True, null=True)),
                ("youtube_url", models.URLField(blank=True, null=True)),
                ("linkedin_url", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("sub_title", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "sub_title_1",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("tab_title", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "image",
                    models.ImageField(default="placeholders/gallery.jpg", upload_to=""),
                ),
                ("description", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("github", models.URLField(blank=True, null=True)),
                ("youtube", models.URLField(blank=True, null=True)),
                ("udemy", models.URLField(blank=True, null=True)),
                ("link_1", models.URLField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Detail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code_title", models.CharField(blank=True, max_length=255, null=True)),
                ("code_url", models.URLField(blank=True, null=True)),
                ("code_notes", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("code", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
            ],
        ),
    ]
