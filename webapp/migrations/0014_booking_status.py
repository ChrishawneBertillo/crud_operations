# Generated by Django 5.1.2 on 2024-12-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_remove_booking_return_date_booking_days_booked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending', max_length=10),
        ),
    ]
