# Generated by Django 5.0.4 on 2024-05-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_alter_family_cell_alter_family_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='update_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
