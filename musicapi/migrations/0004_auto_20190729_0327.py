# Generated by Django 2.2.3 on 2019-07-29 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapi', '0003_auto_20190729_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='music',
            name='image',
            field=models.ImageField(default='media/None/no-img.jpg', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='music',
            name='musicFile',
            field=models.FileField(upload_to='media/'),
        ),
    ]
