# Generated by Django 4.2.11 on 2024-05-30 11:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_question_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(related_name='liked_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
