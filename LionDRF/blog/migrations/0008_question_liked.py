# Generated by Django 5.0.3 on 2024-06-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_question_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
