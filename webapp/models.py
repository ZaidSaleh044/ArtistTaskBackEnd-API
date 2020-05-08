from django.db import models


class albums(models.Model):
    albumName = models.CharField(max_length=10)
    AlbumId = models.IntegerField()
    artistId = models.IntegerField()

    def __str__(self):
        return self.albumName

class artists(models.Model):
    artistName = models.CharField(max_length=10)
    artistId = models.IntegerField()
    imagePath = models.CharField(max_length=100)

    def __str__(self):
        return self.artistName

class songs(models.Model):
    songsName = models.CharField(max_length=10)
    songsId = models.IntegerField()
    artistId = models.IntegerField()
    AlbumId = models.IntegerField()

    def __str__(self):
        return self.songsName

