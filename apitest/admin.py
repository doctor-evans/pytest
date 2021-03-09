from django.contrib import admin

# Register your models here.
from .models import Song, Audiobook, Podcast

admin.site.register(Song)
admin.site.register(Audiobook)
admin.site.register(Podcast)
