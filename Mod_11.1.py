class Julkaisu:
    
    def __init__(self, nimi):
        self.nimi = nimi
        
    
class Kirja(Julkaisu):
    
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)
        
    def tulosta_tiedot(self):
        print(f'Kirjan nimi: {self.nimi}, kirjailija: {self.kirjoittaja}, kirjan sivumäärä: {self.sivumäärä}')
        
class Lehti(Julkaisu):
    
    def __init__(self, nimi,  päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
        
    def tulosta_tiedot(self):
        print(f'Lehden nimi: {self.nimi}, päätoimittaja: {self.päätoimittaja},')
        
akuankka = Lehti('Aku Ankka', 'Aki Hyyppä')
akuankka.tulosta_tiedot()

Hytti_no_6 = Kirja('Hytti no. 6', 'Rosa Liksom', 200)
Hytti_no_6.tulosta_tiedot()