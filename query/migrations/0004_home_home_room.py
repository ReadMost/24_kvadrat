# Generated by Django 2.0.5 on 2018-06-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0003_remove_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='home_room',
            field=models.IntegerField(default=1),
        ),
    ]
