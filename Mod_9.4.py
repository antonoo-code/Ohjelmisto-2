import random

class Auto:
    rekisteritunnus = ''
    huippunopeus = 0
    tämänhetkinen_nopeus = 0
    kuljettu_matka = 0
    
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

    def tulosta_tila(self):
        print(f'Rekisteritunnus: {self.rekisteritunnus}\nHuippunopeus: {self.huippunopeus}\nTämänhetkinen nopeus: {self.tämänhetkinen_nopeus} \nKuljettu matka: {self.kuljettu_matka}')

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        elif self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += (self.tämänhetkinen_nopeus * tuntimäärä)

kilpa_autot = []
for i in range(0,9):
    auto = Auto(f'ABC-{i}', random.randint(100, 200))
    kilpa_autot.append(auto)
kilpailu_käynnissä = True
while kilpailu_käynnissä:
    for auto in kilpa_autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_käynnissä = False
            
    for auto in kilpa_autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        #auto.tulosta_tila()

print(f'\n|  Rekno  | Huippunopeus  | Tämänhetkinen nopeus | Kuljettu matka |')
print(f'+---------+---------------+----------------------+----------------+')
for auto in kilpa_autot:
    print(f'|{auto.rekisteritunnus:>8} ',end='')
    print(f'|{auto.huippunopeus:>14} ',end='')
    print(f'|{auto.tämänhetkinen_nopeus:>21} ',end='')
    print(f'|{auto.kuljettu_matka:>15} |')