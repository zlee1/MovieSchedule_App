# Generated by Django 5.1.4 on 2025-01-10 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.theater'),
        ),
    ]
