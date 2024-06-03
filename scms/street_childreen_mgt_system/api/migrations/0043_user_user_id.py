# Generated by Django 5.0.4 on 2024-05-27 12:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_alter_user_residential_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]