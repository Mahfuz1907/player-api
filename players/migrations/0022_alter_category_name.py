# Generated by Django 5.1.7 on 2025-04-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0021_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(choices=[('A', 'Category A'), ('B', 'Category B'), ('C', 'Category C'), ('D', 'Category D')], default=0),
        ),
    ]
