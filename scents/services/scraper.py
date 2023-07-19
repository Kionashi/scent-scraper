import decimal
from typing import List
from bs4 import BeautifulSoup
import requests
import re
from scents.models.accord import Accord

from scents.models.designer import Designer
from scents.models.family import Family
from scents.models.note import Note
from scents.models.perfumeaccord import PerfumeAccord
from scents.models.perfumenote import PerfumeNote
from ..models.perfume import Perfume
from ..models.perfumer import Perfumer

class ScraperService():

    def perfume_detail(self, url: str) -> Perfume:  
        """ Scrap the given perfume detail url to create a new Perfume with all their related models"""
        print(f'Scraping this url {url}')
        agent = {"User-Agent":"Mozilla/5.0"} # Add User-Agent to bypass anti bot protections >:D #Hackerman
        result = requests.get(url,headers=agent).text
        doc = BeautifulSoup(result, "html.parser")
        if doc != None:
            perfume_name = doc.find("h1").text # Find the first element with <h1> tag and return the text inside that tag
            perfume = Perfume.objects.filter(name=perfume_name).first()
            if not perfume:
                perfume = Perfume()
                perfume.name = perfume_name

            description = doc.find("div",itemprop="description") # Find the first <div> tag with attribute itemprop="description"
            description = description.find("p").text # Find the first <p> tag inside the previous div tag and return the text inside that tag
            perfume.description = description
            
            category_tag_unisex = doc.find("small", text="para Hombres y Mujeres")
            category_tag_man = doc.find("small", text="para Hombres")
            category_tag_woman = doc.find("small", text="para Mujeres")

            if category_tag_unisex:
                perfume.category = Perfume.Categories.UNISEX
            if category_tag_man:
                perfume.category = Perfume.Categories.MAN
            if category_tag_woman:
                perfume.category = Perfume.Categories.WOMAN

            # main_img = doc.find("img",alt=perfume_name)['src']
            main_img = doc.find("img",itemprop="image")['src']
            perfume.image = main_img
            
            brand = doc.find("p",itemprop="brand")
            designer_name = brand.find("span").text
            designer = Designer.objects.filter(name=designer_name).first()
            if not designer:
                designer = Designer()
                designer.name = designer_name
                designer.save()
            else:
                print('Designer actually exists!!')
            perfume.designer = designer
            
            perfume.save()

            perfumer_img_tags = doc.find_all("img",class_="perfumer-avatar")
            perfumers = []
            for img in perfumer_img_tags:
                perfumer_name = img.parent()[1].text
                perfumer = Perfumer.objects.filter(name=perfumer_name).first()
                if not perfumer:
                    perfumer = Perfumer()
                    perfumer.name = perfumer_name
                    perfumer.save()
                else:
                    print('Perfumer actually exists!!')
                perfumers.append(perfumer)
            
            perfume.perfumers.set(perfumers) # Set perfumers
            
            # Clear the existing PerfumeNote relationships for the perfume
            PerfumeNote.objects.filter(perfume=perfume).delete()

            plain = doc.find("pyramid-level", notes="ingredients")
            if plain:
                for content in plain.contents[0].contents:
                    note_name = content.contents[1].text
                    note = Note.objects.filter(name=note_name).first()
                    if not note:
                        note = Note.objects.create(name=note_name)
                    PerfumeNote.objects.create(perfume=perfume, note=note, position=PerfumeNote.Positions.PLAIN)

            top = doc.find("pyramid-level", notes="top")
            if top:
                for content in top.contents[0].contents:
                    note_name = content.contents[1].text
                    note = Note.objects.filter(name=note_name).first()
                    if not note:
                        note = Note.objects.create(name=note_name)
                    PerfumeNote.objects.create(perfume=perfume, note=note, position=PerfumeNote.Positions.TOP)
            
            middle = doc.find("pyramid-level", notes="middle")
            if middle:
                for content in middle.contents[0].contents:
                    note_name = content.contents[1].text
                    note = Note.objects.filter(name=note_name).first()
                    if not note:
                        note = Note()
                        note.name = note_name
                        note.save()
                    
                    PerfumeNote.objects.create(perfume=perfume, note=note, position=PerfumeNote.Positions.MID)
            
            base = doc.find("pyramid-level", notes="base")
            if base:
                for content in base.contents[0].contents:
                    note_name = content.contents[1].text
                    note = Note.objects.filter(name=note_name).first()
                    if not note:
                        note = Note()
                        note.name = note_name
                        note.save()
                    PerfumeNote.objects.create(perfume=perfume, note=note, position=PerfumeNote.Positions.BOT)

            # Clear the existing PerfumeAccord relationships for the perfume
            PerfumeAccord.objects.filter(perfume=perfume).delete()
            accords_bars = doc.find_all("div",class_='accord-bar')
            for accord_bar in accords_bars:
                # print(accord_bar)
                accord_name = accord_bar.text
                accord = Accord.objects.filter(name=accord_name).first()
                if not accord:
                    accord = Accord()
                    accord.name = accord_name
                    accord.save()
                styles = accord_bar['style'].split(';')
                for style in styles:
                    match = re.search('width:',style)
                    if match:
                        accord_width = match.string[match.end():]
                        accord_concentration = float(accord_width.strip('%')) # Remove % from the end and convert to decimal number that is more precise than the float
                        PerfumeAccord.objects.create(perfume=perfume, accord=accord, concentration=accord_concentration)
            return perfume
        else:
            print('===============ERROR================')
            print(f'error getting this perfume url {url}')

    def family_list(self) -> List[str]:
        """ Scrap the family list to create all the families and get the a list of urls from all family details which contains the links to every perfume detail"""
        url = 'https://www.fragrantica.es/grupo/'
        results = []
        agent = {"User-Agent":"Mozilla/5.0"}
        response = requests.get(url,headers=agent).text
        doc = BeautifulSoup(response, "html.parser")
        if doc != None:
            sections = doc.find_all('div',class_="grid-x grid-padding-x")
            for section in sections:
                section = section.contents
                family_parent_name = section[1].find('a').string
                family_parent_hero_image = section[1].find('img')['src']
                parent = Family.objects.filter(name=family_parent_name).first()
                if not parent:
                    parent = Family()
                    parent.name = family_parent_name
                    parent.hero_image = family_parent_hero_image
                    parent.save()
                url = section[3].find('a')['href']
                url = self.set_base_url(url)
                item = {
                    'url': url,
                    'family_id': parent.id
                }
                results.append(item)
                children_tag = section[5].find_all('a')
                for child_tag in children_tag:
                    child_name = child_tag.find('b').string
                    child_url = self.set_base_url(child_tag['href'])
                    child = Family.objects.filter(name=child_name).first()
                    if not child:
                        child = Family()
                        child.name = child_name
                        child.parent = parent
                        child.save()
                    item = {
                        'url': child_url,
                        'family_id': child.id
                    }
                    results.append(item)
            return results
        else:
            print('===============ERROR================')
            print('Error getting family url')

    def family_detail(self, family_url:str) ->List[dict]:
        """ Scrap the family detail page and returns a list of all the urls to the details of every perfume in the list with the year of creation"""
        results = []
        agent = {"User-Agent":"Mozilla/5.0"}
        result = requests.get(family_url,headers=agent).text
        doc = BeautifulSoup(result, "html.parser")
        if doc != None:
            cards = doc.find_all('div',class_='cell large-6')
            for card in cards:
                item = {}
                url = card.find('a')['href']
                url = self.set_base_url(url)
                item['url'] = url
                item['year'] = card.find_all('span')[-1].string
                results.append(item)
        else:
            print('===============ERROR================')
            print(f'Error getting this family url {family_url}')
        return results
    
    def set_base_url(self, url: str) ->str:
        if url.find('https://www.fragrantica.es') == -1:
            url = 'https://www.fragrantica.es'+url
        return url
