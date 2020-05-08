from django.contrib import admin
from . models import albums
from . models import artists
from . models import songs

admin.site.register(albums)
admin.site.register(artists)
admin.site.register(songs)
# Register your models here.
