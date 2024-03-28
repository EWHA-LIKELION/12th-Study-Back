# Generated by Django 5.0.3 on 2024-03-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Title')),
                ('upload_time', models.DateTimeField(unique=True)),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
    ]
