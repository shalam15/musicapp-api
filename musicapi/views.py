from django.shortcuts import render
from rest_framework import viewsets
from .models import Music
from .serializers import MusicSerializer

class MusicView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer