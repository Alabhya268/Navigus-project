# Generated by Django 3.0.5 on 2021-06-27 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20210627_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
