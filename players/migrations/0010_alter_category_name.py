# Generated by Django 5.1.7 on 2025-04-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=0, max_length=20),
        ),
    ]
