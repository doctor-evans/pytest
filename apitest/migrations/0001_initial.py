# Generated by Django 3.1.4 on 2021-03-08 23:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('time_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('time_added', models.DateTimeField(auto_now=True)),
                ('Host', models.CharField(max_length=100)),
                ('participant', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=10)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('time_added', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]