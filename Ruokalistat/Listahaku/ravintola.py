"""Ravintola-olion määrittely"""
class ravintola:
    def __init__(self, nimi, hinta, ruoat):
        self.nimi = nimi
        self.hinta = hinta
        self.ruoat = ruoat

    def __str__(self):
        nl = '\n'
        return f"{self.nimi} - lounas {self.hinta}€\n{nl.join(self.ruoat)}"

    def nimi(self):
        return f"{self.nimi}"

    def hinta(self):
        return f"{self.hinta}"

    def lounas(self):
        nl = '\n'
        return f"{nl.join(self.ruoat)}"