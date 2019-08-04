from django.shortcuts import render
from rest_framework import viewsets
from .models import Artiste
from .serializers import ArtisteSerializer



class ArtisteView(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer