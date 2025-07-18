# Generated by Django 5.2.1 on 2025-07-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='github_url',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=130, unique=True),
        ),
    ]
