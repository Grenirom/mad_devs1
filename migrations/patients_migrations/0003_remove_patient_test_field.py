# Generated by Django 5.1.5 on 2025-01-25 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0002_patient_test_field"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="test_field",
        ),
    ]
