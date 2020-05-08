# Generated by Django 3.0.5 on 2020-04-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alboms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albomName', models.CharField(max_length=10)),
                ('AlbomId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=10)),
                ('artistId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songsName', models.CharField(max_length=10)),
                ('songsId', models.IntegerField()),
            ],
        ),
    ]
