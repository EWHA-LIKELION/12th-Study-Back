# Generated by Django 5.0.4 on 2024-05-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0017_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_like',
            field=models.BooleanField(default=False, verbose_name='좋아요'),
        ),
        migrations.AddField(
            model_name='question',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
