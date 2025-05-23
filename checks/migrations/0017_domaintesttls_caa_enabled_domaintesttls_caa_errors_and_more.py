# Generated by Django 4.2.18 on 2025-02-12 10:21

import checks.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checks", "0016_webtestappsecpriv_timestamp_webtesttls_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="domaintesttls",
            name="caa_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="domaintesttls",
            name="caa_errors",
            field=checks.models.ListField(default=[]),
        ),
        migrations.AddField(
            model_name="domaintesttls",
            name="caa_found_on_domain",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="domaintesttls",
            name="caa_recommendations",
            field=checks.models.ListField(default=[]),
        ),
        migrations.AddField(
            model_name="domaintesttls",
            name="caa_score",
            field=models.IntegerField(null=True),
        ),
    ]
