import graphene
from graphene_django import DjangoObjectType

from . models import songs, albums, artists


class SongType(DjangoObjectType):
    class Meta:
        model = songs


class ArtistType(DjangoObjectType):
    class Meta:
        model = artists


class AlbumType(DjangoObjectType):
    class Meta:
        model = albums


class Query(graphene.ObjectType):
    songs = graphene.List(SongType)
    artists = graphene.List(ArtistType)
    albums = graphene.List(AlbumType)

    def resolve_songs(self, info, **kwargs):
        return songs.objects.all()

    def resolve_albums(self, info, **kwargs):
        return albums.objects.all()

    def resolve_artists(self, info, **kwargs):
        return artists.objects.all()



