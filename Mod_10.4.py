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


class Kilpailu:
    kilpailun_nimi = ''
    kilpaulun_pituus_km = 0
    osallistuvat_autot = []
    
    def __init__(self, kilpailun_nimi, kilpailun_pituus_km, osallistuvat_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpaulun_pituus_km = kilpailun_pituus_km
        self.osallistuvat_autot = osallistuvat_autot
    
    def tunti_kuluu(self):
        for auto in self.osallistuvat_autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
            
    def tulosta_tilanne(self):
        print(f'\n|  Rekno  | Huippunopeus  | Tämänhetkinen nopeus | Kuljettu matka |')
        print(f'+---------+---------------+----------------------+----------------+')
        for auto in self.osallistuvat_autot:
            print(f'|{auto.rekisteritunnus:>8} ',end='')
            print(f'|{auto.huippunopeus:>14} ',end='')
            print(f'|{auto.tämänhetkinen_nopeus:>21} ',end='')
            print(f'|{auto.kuljettu_matka:>15} |')
            
    def kilpailu_ohi(self,):
        for auto in self.osallistuvat_autot:
            if auto.kuljettu_matka >= self.kilpaulun_pituus_km:
                return True
        return False


osallistuvat_autot_lista = []      

for i in range(0,9):
    osallistuvat_autot_lista.append(Auto(f'ABC-{i}', random.randint(100, 200)))

kisa = Kilpailu('Suuri romuralli', 8000, osallistuvat_autot_lista)
i = 0
while kisa.kilpailu_ohi() == False:
    kisa.tunti_kuluu()
    i += 1
    if i % 10 == 0:
        kisa.tulosta_tilanne()
kisa.tulosta_tilanne()

