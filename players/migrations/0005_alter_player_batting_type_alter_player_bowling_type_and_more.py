# Generated by Django 5.1.7 on 2025-04-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_category_alter_player_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='batting_type',
            field=models.CharField(choices=[('Right Arm Batsman', 'Right Arm Batsman'), ('Left Arm Batsman', 'Left Arm Batsman')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='bowling_type',
            field=models.CharField(choices=[('Right Arm Fast', 'Right Arm Fast'), ('Left Arm Fast', 'Left Arm Fast'), ('Right Arm Off Spin', 'Right Arm Off Spin'), ('Left Arm Off Spin', 'Left Arm Off Spin'), ('Right Arm Leg Spin', 'Right Arm Leg Spin'), ('Left Arm Leg Spin', 'Left Arm Leg Spin')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='role',
            field=models.CharField(choices=[('Batsman', 'Batsman'), ('Bowler', 'Bowler'), ('Batting All-rounder', 'Batting All-rounder'), ('Bowling All-rounder', 'Bowling All-rounder')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(choices=[('Pak', 'Pakistan'), ('Ban', 'Bangladesh')], default='', max_length=100),
        ),
    ]
