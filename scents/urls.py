from django.urls import path, include
from rest_framework import routers

from .views.scraper import ScraperView

router = routers.DefaultRouter()
router.register(r'scraper', ScraperView, basename='scraper')

urlpatterns = [
    path('', include(router.urls)),
]