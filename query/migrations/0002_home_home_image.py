# Generated by Django 2.0.5 on 2018-05-30 15:09

from django.db import migrations, models
import query.models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='home_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=query.models.get_image_path),
        ),
    ]
