# Generated by Django 4.2.3 on 2023-08-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_clientmodel_spent_money"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientmodel",
            name="spent_money",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name="purchasemodel",
            name="total",
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]