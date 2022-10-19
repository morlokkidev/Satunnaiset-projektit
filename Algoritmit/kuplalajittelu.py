def kuplalajittelu(lista):
    """Yksinkertainen lajittelufunktio, joka palauttaa pienimmästä suurimpaan lajitellun listan"""
    #Sijoitetaan listan viimeisen elementin indeksi muuttujaan 'viimeinen' luettavuuden parantamiseksi
    viimeinen = len(lista)-1
    #Listan pienin ja suurin alustetaan ensimmäiseen elementtiin
    suurin, pienin = lista[0], lista[0]

    #Käydään lista läpi kahteen otteeseen, jotta saadaan tietoon listan pienin ja suurin elementti 
    #Tarkoituksella jätetty käyttämättä min() ja max() funktioita
    for n in lista:
        if n > suurin:
            suurin = n
    for n in lista:
        if n < pienin:
            pienin = n
    
    #Käydään listaa läpi, kunnes listan ensimmäinen elementti on pienin ja viimeinen elementti suurin
    #Tässä tapauksessa luodaan muuttuja muutos, jonka arvo muutetaan joka kierroksella ensin epätodeksi ja sen jälkeen todeksi jos listaa läpikäydessä ilmenee muutoksia
    muutos = True
    while muutos:
        muutos = False
        for i in range(viimeinen):
            #Jos läpikäytävä elementti on suurempi kuin listan seuraava elementti, vaihdetaan niiden paikkaa
            if lista[i] > lista [i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                #Muutos tapahtunut, muutetaan arvo todeksi, jotta kierros käydään uudelleen
                muutos = True

    #Palautetaan lajiteltu lista
    return lista