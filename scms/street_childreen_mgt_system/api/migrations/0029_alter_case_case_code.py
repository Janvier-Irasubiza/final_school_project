# Generated by Django 5.0.4 on 2024-05-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_alter_family_cell_alter_family_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_code',
            field=models.CharField(blank=True, editable=False, max_length=100, unique=True),
        ),
    ]