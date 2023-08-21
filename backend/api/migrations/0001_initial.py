# Generated by Django 4.2.3 on 2023-08-21 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClientModel",
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
                ("username", models.CharField(max_length=80)),
                ("spent_money", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name="GemModel",
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
                ("name", models.CharField(max_length=80)),
                (
                    "client",
                    models.ManyToManyField(related_name="gems", to="api.clientmodel"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseModel",
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
                ("total", models.DecimalField(decimal_places=2, max_digits=8)),
                ("quantity", models.IntegerField()),
                ("date", models.DateTimeField()),
                (
                    "gem",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchases",
                        to="api.gemmodel",
                    ),
                ),
            ],
        ),
    ]
