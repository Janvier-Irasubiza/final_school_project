# Generated by Django 5.0.4 on 2024-05-11 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_case_case_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='cell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cell'),
        ),
        migrations.AlterField(
            model_name='family',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sector'),
        ),
    ]
