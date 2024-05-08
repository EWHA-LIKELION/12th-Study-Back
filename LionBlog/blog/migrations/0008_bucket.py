# Generated by Django 5.0.3 on 2024-05-01 15:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_question_likes_delete_article'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_buckets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
