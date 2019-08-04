# Generated by Django 2.2.3 on 2019-07-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('worldRank', models.IntegerField()),
                ('musicGenre', models.CharField(choices=[(1, 'hipHop'), (1, 'pop')], max_length=1)),
                ('origin', models.CharField(max_length=120)),
                ('originFlag', models.CharField(max_length=120)),
            ],
        ),
    ]