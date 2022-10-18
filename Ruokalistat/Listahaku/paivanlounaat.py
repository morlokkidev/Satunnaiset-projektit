from bs4 import BeautifulSoup, SoupStrainer
from Listahaku.ravintola import ravintola
import Listahaku.constants as const
import cfscrape
import requests
import datetime
import re

"""Lounasten haku moduuli. Ravintolat ja päivän tajonnat tallennetaan olioihin ja metodin lopussa palautetaan ruokalista merkkijonona"""

#f-merkkijonot eivät tykkää käsitellä \/ merkkejä, sisällytetään rivinvaihto muuttujan sisään
nl = '\n'

def haePaivanLounaat():

    #Haetaan Panchon lounaat
    url = const.URL_PANCHO
    result = requests.get(url)
    panchosoppa = BeautifulSoup(result.text, 'html.parser', parse_only=SoupStrainer(id="Lounas"))
    lounaat = panchosoppa.find_all("p")
    #irroitetaan listasta hintatiedot
    lounaat.pop(0)
    #haetaan tämän päivän lounas ja irroitetaan turhat tiedot
    lounas = str.splitlines(lounaat[datetime.datetime.weekday(datetime.datetime.now())].text)
    lounas.pop(0)
    #luodaan pancho-olio
    pancho = ravintola("Pancho Villa", 11.30, lounas)

    #Haetaan Portin lounaat
    url = const.URL_PORTTI
    result = requests.get(url)
    #Portilla cloudflare bottisuojaus, käytetään cloudflare-scrape työkalua suojakusen ohittamiseksi
    scraper = cfscrape.create_scraper()
    porttisoppa = BeautifulSoup(scraper.get(url).content, 'html.parser')
    for strong in porttisoppa("strong"):
        strong.decompose()
    for x in range(2):
        porttisoppa.p.decompose()
    lounaslista = porttisoppa.find_all("p")
    lounas = str.splitlines(lounaslista[datetime.datetime.weekday(datetime.datetime.now())].text)
    #Luodaan portti-olio
    portti = ravintola("Ravintola Portti", 11.30, lounas)

    #Haetaan Salpaparkin luonaat
    url = const.URL_SALPA
    result = requests.get(url)
    salpasoppa = BeautifulSoup(result.text, 'html.parser', parse_only=SoupStrainer(id="comp-k4r0qbgu"))
    salpasoppa.div.unwrap()
    #Erotellaan ruokalista päivien mukaan hyödyntäen regex, irroitetaan turha elementti ja haetaan päivän lounas
    viikonpvregex = "|".join(const.VIIKONPAIVATNIMI)
    lounaat = re.split(f'{viikonpvregex}',salpasoppa.text)
    lounaat.pop(0)
    lounas = str.splitlines(lounaat[datetime.datetime.weekday(datetime.datetime.now())])
    #poistetaan ruokalistasta esiintymät, jotka eivät ala kirjaimella
    for i in enumerate(lounas):
        if lounas[i[0]][0].isalpha():
            pass
        else:
            lounas.pop(i[0])
    #luodaan salpa-olio
    salpa = ravintola("Salpaparkki",11.30,lounas)

    #Palautetaan oliot
    return f"{portti.nimi} - {portti.hinta}€{nl}{portti.lounas()}{nl}{nl}{salpa.nimi} - {salpa.hinta}€{nl}{salpa.lounas()}{nl}{nl}{pancho.nimi} - {pancho.hinta}€{nl}{pancho.lounas()}"

