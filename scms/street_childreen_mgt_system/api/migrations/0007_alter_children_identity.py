# Generated by Django 5.0.4 on 2024-05-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_case_reported_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='identity',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]