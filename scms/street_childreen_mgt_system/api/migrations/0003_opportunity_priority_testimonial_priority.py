# Generated by Django 5.0.4 on 2024-05-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_case_case_desc_alter_opportunity_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='priority',
            field=models.CharField(default='general', max_length=50),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='priority',
            field=models.CharField(default='general', max_length=50),
        ),
    ]
