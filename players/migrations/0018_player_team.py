# Generated by Django 5.1.7 on 2025-04-05 01:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0017_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='players.team'),
        ),
    ]
