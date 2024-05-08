# Generated by Django 3.2.25 on 2024-05-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='hashtag',
            field=models.ManyToManyField(to='community.HashTag'),
        ),
    ]
