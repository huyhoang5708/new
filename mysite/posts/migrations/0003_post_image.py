# Generated by Django 5.0.2 on 2024-03-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(height_field=500, max_length=500, null=True, upload_to=None, verbose_name='images/', width_field=500),
        ),
    ]
