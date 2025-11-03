class Auto:
    rekisteritunnus = ''
    huippunopeus = 0
    tämänhetkinen_nopeus = 0
    kuljettu_matka = 0
    
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

    def tulosta_tila(self):
        print(f'Rekisteritunnus: {Possu.rekisteritunnus}\nHuippunopeus: {Possu.huippunopeus}\nTämänhetkinen nopeus: {Possu.tämänhetkinen_nopeus} \nKuljettu matka: {Possu.kuljettu_matka}')

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        elif self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

    def kulje(self, tuntimäärä):
        self.kuljettu_matka + (self.tämänhetkinen_nopeus * tuntimäärä)

Possu = Auto('ABC-123', 142)
Possu.kiihdytä(30)
Possu.kiihdytä(70)
Possu.kiihdytä(50)
print(f'Auton nopeus: {Possu.tämänhetkinen_nopeus}')
Possu.kiihdytä(-200)
print(f'Auton nopeus: {Possu.tämänhetkinen_nopeus}')