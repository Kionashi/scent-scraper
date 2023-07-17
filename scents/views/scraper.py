
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

        perfume = self.scraper_service.perfume_detail('https://www.fragrantica.es/perfume/19-69/La-Habana-65418.html')
        total = 0
       
        """  family_urls = self.scraper_service.family_list()
        for family_url in family_urls:
            perfume_urls = self.scraper_service.family_detail(family_url)
            for perfume_url in perfume_urls:
                perfume = self.scraper_service.perfume_detail(perfume_url['url'])
                perfume.creation_year = perfume_url['year']
                perfume.save()
                print(f'perfume {perfume.name} created!')
                total+=1 """


        return Response(f'Created {total} perfumes :D', status.HTTP_200_OK)
            
        
