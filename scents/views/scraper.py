
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..services.scraper import ScraperService
class ScraperView(viewsets.ViewSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scraper_service = ScraperService()

    @action(detail=False, methods=['GET'], url_path='test')
    def test(self,request):
        url = 'https://www.fragrantica.es/perfume/Paco-Rabanne/1-Million-3747.html'
        url='https://www.fragrantica.es/perfume/Bud-Parfums/Assassin-12056.html'
        url='https://www.fragrantica.es/perfume/Amberfig/Bamboo-Green-Tea-30473.html'
        self.scraper_service.perfume_detail(url)
        return Response('title', status.HTTP_200_OK)
            
        
