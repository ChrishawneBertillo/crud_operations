# Generated by Django 5.1.2 on 2024-12-12 09:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_customer_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='feedback_text',
        ),
        migrations.AddField(
            model_name='feedback',
            name='bike',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.bike'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='text',
            field=models.TextField(default='Default feedback text'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
