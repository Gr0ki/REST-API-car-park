# Generated by Django 4.0 on 2021-12-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_driver', '0008_alter_driver_created_at_alter_driver_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='created_at',
            field=models.DateField(blank=True, default='13/12/2021'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='updated_at',
            field=models.DateField(blank=True, default='13/12/2021'),
        ),
    ]