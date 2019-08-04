from rest_framework import serializers
from .models import Artiste

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ('id','firstName', 'lastName', 'worldRank', 'musicGenre', 'origin', 'originFlag', 'avatarImage')