from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("encode", ShortenerViewSet, basename="encode")
router.register("decode", LengthenerViewSet, basename="decode")


urlpatterns = [
    path("", include(router.urls)),
    path("<str:short_url>", redirect_to_long_url),
]