from rest_framework import serializers
from .models import Hotdog


class HotdogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotdog
        fields = ('name', 'link')
