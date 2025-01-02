# Generated by Django 5.1.2 on 2024-10-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_bike_booking_customer_delete_person_booking_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='customer_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]