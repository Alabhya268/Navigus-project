# Generated by Django 3.0.5 on 2021-06-27 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20210626_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='passing_marks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='answer1',
            field=models.CharField(blank=True, choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4')], max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='answer2',
            field=models.CharField(blank=True, choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4')], max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='answer3',
            field=models.CharField(blank=True, choices=[('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4')], max_length=200),
        ),
    ]
