# Generated by Django 5.1.2 on 2025-01-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_alter_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='due_date',
            field=models.DateField(blank=True, editable=False, null=True),
        ),
    ]