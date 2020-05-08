from rest_framework import serializers
from . models import albums
from . models import artists
from . models import songs



class albumSerlizer(serializers.ModelSerializer):

    class Meta:
        model = albums
        fields=('albumName')
        fields='__all__'


class artistSerlizer(serializers.ModelSerializer):

    class Meta:
        model = artists
        fields=('artistName')
        fields='__all__'


class songSerlizer(serializers.ModelSerializer):

    class Meta:
        model = songs
        fields=('songName')
        fields='__all__'