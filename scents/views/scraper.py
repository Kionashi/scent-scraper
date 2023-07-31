
import time
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

        total = 0
        """
        """
        family_url_items = self.scraper_service.family_list()
        # self.scraper_service.process_families(family_url_items)
        self.scraper_service.process_perfumes()        
        return Response(f'Created {total} perfumes :D', status.HTTP_200_OK)
            
        
