
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from bs4 import BeautifulSoup
import requests
import re

class ScraperView(viewsets.ViewSet):
    @action(detail=False, methods=['GET'], url_path='test')
    def test(self,request):
        url = 'https://www.fragrantica.es/perfume/Paco-Rabanne/1-Million-3747.html'
        url='https://www.fragrantica.es/perfume/Bud-Parfums/Assassin-12056.html'
        url='https://www.fragrantica.es/perfume/Amberfig/Bamboo-Green-Tea-30473.html'
        agent = {"User-Agent":"Mozilla/5.0"} # Add User-Agent to bypass anti bot protections >:D
        try:
            result = requests.get(url,headers=agent).text
            doc = BeautifulSoup(result, "html.parser")
            if doc != None:
                title = doc.find("h1").text # Find the first element with <h1> tag and return the text inside that tag
            
                description = doc.find("div",itemprop="description") # Find the first <div> tag with attribute itemprop="description"
                description = description.find("p").text # Find the first <p> tag inside the previous div tag and return the text inside that tag
                
                brand = doc.find("p",itemprop="brand")
                brand_name = brand.find("span").text
                
                img_tags = doc.find_all("img",class_="perfumer-avatar")
                perfumers = []
                for img in img_tags:
                    perfumer_name = img.parent()[1].text
                    perfumers.append(perfumer_name)
                
                main_img = doc.find("img",alt=title)
                main_img = doc.find("img",itemprop="image")
                
                top = doc.find("pyramid-level", notes="top")
                top_notes = []
                for content in top.contents[0].contents:
                    top_notes.append(content.contents[1].text)

                middle = doc.find("pyramid-level", notes="middle")
                middle_notes = []
                for content in middle.contents[0].contents:
                    middle_notes.append(content.contents[1].text)
                
                base = doc.find("pyramid-level", notes="base")
                base_notes = []
                for content in base.contents[0].contents:
                    base_notes.append(content.contents[1].text)

                print('===============TAG================')
                accords_bars = doc.find_all("div",class_='accord-bar')
                accords = []
                for accord_bar in accords_bars:
                    # print(accord_bar)
                    accord = dict()
                    accord['name'] = accord_bar.text
                    styles = accord_bar['style'].split(';')
                    for style in styles:
                        match = re.search('width:',style)
                        if match:
                            accord['width'] = match.string[match.end():]
                    accords.append(accord)
                print(accords)
                return Response(title, status.HTTP_200_OK)
            else:
                print('===============ERROR================')
        except Exception as error:
            print('errror:', error)
            return Response(status.HTTP_400_BAD_REQUEST)
