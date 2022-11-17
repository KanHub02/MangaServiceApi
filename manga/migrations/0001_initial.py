# Generated by Django 4.1.3 on 2022-11-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
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
                ("title", models.CharField(max_length=250)),
            ],
            options={
                "verbose_name": "Жанр",
                "verbose_name_plural": "Жанры",
            },
        ),
        migrations.CreateModel(
            name="Translator",
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
                ("title", models.CharField(max_length=150)),
                ("image", models.ImageField(upload_to="")),
            ],
            options={
                "verbose_name": "Дубляж",
                "verbose_name_plural": "Дубляж",
            },
        ),
        migrations.CreateModel(
            name="Manga",
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
                ("en_name", models.CharField(max_length=200)),
                ("ru_name", models.CharField(max_length=200)),
                ("image", models.TextField()),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("type", models.CharField(max_length=100)),
                ("likes", models.PositiveIntegerField()),
                ("rating", models.FloatField(blank=True, default=0.0)),
                ("genre", models.ManyToManyField(to="manga.genre")),
                ("translator", models.ManyToManyField(to="manga.translator")),
            ],
            options={
                "verbose_name": "Манга",
                "verbose_name_plural": "Манга",
            },
        ),
    ]
