# Generated by Django 5.0.4 on 2024-06-01 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_opportunity_slag_testimonial_slag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='slag',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='slag',
            field=models.CharField(max_length=100),
        ),
    ]