# Generated by Django 5.0.5 on 2024-05-23 10:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_question_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='upload_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
