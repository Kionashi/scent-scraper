import decimal
from bs4 import BeautifulSoup
import requests
import re
from scents.models.accord import Accord

from scents.models.designer import Designer
from scents.models.note import Note
from scents.models.perfumeaccord import PerfumeAccord
from scents.models.perfumenote import PerfumeNote
from ..models.perfume import Perfume
from ..models.perfumer import Perfumer

class ScraperService():

    def perfume_detail(self, url: str):
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

            top = doc.find("pyramid-level", notes="top")
            for content in top.contents[0].contents:
                note_name = content.contents[1].text
                note = Note.objects.filter(name=note_name).first()
                print(f'--------CHECKING THIS NOTE {note}----------------------')
                if not note:
                    print('/////////////////////////NOT NOTE////////////////')
                    note = Note.objects.create(name=note_name)
                PerfumeNote.objects.create(perfume=perfume, note=note, position=PerfumeNote.Positions.TOP)
            
            middle = doc.find("pyramid-level", notes="middle")
            for content in middle.contents[0].contents:
                note_name = content.contents[1].text
                note = Note.objects.filter(name=note_name).first()
                if not note:
                    note = Note()
                    note.name = note_name
                    note.save()
                
                PerfumeNote.objects.create(perfume=perfume, note=note, position=PerfumeNote.Positions.MID)
            
            base = doc.find("pyramid-level", notes="base")
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
            print('===============TAG================')
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
        else:
            print('===============ERROR================')