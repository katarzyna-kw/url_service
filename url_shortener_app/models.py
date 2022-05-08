# 1. create Shortener model
# -- attributes: long url, short url -- can be blank, must be unique
# create hash for short urls
# -- helper function to create random hash/string of letters/digits
# -- helper function to assign hash and check if hash already used
# modify save method on Shortener class to call helper function to create short url for this instance, then save
# 2. create Shortener serializer 
# 3. Shortener Viewset
# 4. urls.py for Shortener Viewset with /encode endpoint
# 5. HttpResponseRedirect to redirect short url to long url
# 6. Create Serializer/ViewSet for Lengthener and /decode route
# 7. Modify serializer create methods -- check if obj exists first and create only if not
# 8. README file

from django.db import models
from .utils import BASE_URL, generate_sequence_for_short_url

class Shortener(models.Model):
    long_url = models.URLField(blank=True, unique=True)
    short_url = models.CharField(max_length=35, unique=True, blank=True)
    
    def __str__(self):
        return f"{self.long_url} shortened to {self.short_url}"
    
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = f"{BASE_URL}{generate_sequence_for_short_url(self)}"
            
        super().save(*args, **kwargs)