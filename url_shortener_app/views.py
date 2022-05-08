from django.http import Http404
from .models import Shortener
from .serializers import ShortenerSerializer
from rest_framework.viewsets import ModelViewSet
from .utils import BASE_URL
from django.http import HttpResponseRedirect, Http404

class ShortenerViewSet(ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer
    
    def get_queryset(self):
        return Shortener.objects.all().order_by("-id")
    
    
def redirect_to_long_url(request, short_url):
    try:
        shortener = Shortener.objects.get(short_url=f"{BASE_URL}{short_url}")
        return HttpResponseRedirect(shortener.long_url)
    
    except:
        raise Http404("Something went wrong. Please try again.")