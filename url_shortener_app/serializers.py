from rest_framework import serializers
from .models import Shortener


class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ["id", "long_url", "short_url"]
    
    long_url = serializers.URLField()
    short_url = serializers.CharField(allow_null=True, read_only=True)
    
    
class LengthenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ["id", "long_url", "short_url"]

    long_url = serializers.URLField(allow_null=True, read_only=True)
    short_url = serializers.CharField()