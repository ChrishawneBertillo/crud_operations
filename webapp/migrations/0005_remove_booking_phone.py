# Generated by Django 5.1.2 on 2024-10-23 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_booking_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='phone',
        ),
    ]