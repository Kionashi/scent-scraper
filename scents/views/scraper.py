
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
        family_url_items = self.scraper_service.family_list()
        self.scraper_service.process_families(family_url_items)
        """ try:
            for family_url_item in family_url_items:
                print(family_url_item['url'])
                family_id = int(family_url_item['family_id'])
                perfume_urls = self.scraper_service.family_detail(family_url_item['url'])
                for perfume_url in perfume_urls:
                    perfume = self.scraper_service.perfume_detail(perfume_url['url'])
                    perfume.creation_year = perfume_url['year']
                    perfume.family_id = family_id
                    perfume.save()
                    print(f'perfume {perfume.name} created/edited!')
                    total+=1
                    time.sleep(10)
        except Exception as e:
            print('Exception!!')
            time.sleep(600) """
        
        return Response(f'Created {total} perfumes :D', status.HTTP_200_OK)
            
        
