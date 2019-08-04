from django.contrib.auth.models import User
from artisteapi.models import Artiste
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password')
