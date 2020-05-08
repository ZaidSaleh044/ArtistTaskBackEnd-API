from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import albums
from . models import artists
from . models import songs
from .serializers import albumSerlizer
from .serializers import artistSerlizer
from .serializers import songSerlizer

# class

class albumList(APIView):
    def get(self,request):
        album=albums.objects.all()
        serlizer=albumSerlizer(album,many=True)
        return Response(serlizer.data)

    def post(self):
        pass


class artistList(APIView):
    def get(self,request):
        artist=artists.objects.all()
        serlizer=artistSerlizer(artist,many=True)
        return Response(serlizer.data)

    def post(self):
        pass


class songList(APIView):
    def get(self,request):
        song=songs.objects.all()
        serlizer=songSerlizer(song,many=True)
        return Response(serlizer.data)

    def post(self):
        pass