# Generated by Django 5.0.3 on 2024-05-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_hashtag_question_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
