# Generated by Django 4.2.11 on 2024-05-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('language', models.IntegerField(choices=[(1, 'KOR'), (2, 'ENG'), (3, 'JPN'), (4, 'CHN')])),
            ],
        ),
    ]
