from .models import Shortener
from .serializers import ShortenerSerializer
from rest_framework.viewsets import ModelViewSet
from .utils import BASE_URL
from django.shortcuts import render

class ShortenerViewSet(ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer
    
    def get_queryset(self):
        return Shortener.objects.all().order_by("-id")