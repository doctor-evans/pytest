from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    time_added = models.DateTimeField(auto_now=True)

class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    time_added = models.DateTimeField(auto_now=True)
    Host = models.CharField(max_length=100)
    participant = ArrayField(models.CharField(max_length=100), size=10, null=True, blank=True)

class Audiobook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    time_added = models.DateTimeField(auto_now=True)
