class Auto:
    rekisteritunnus = ''
    huippunopeus = 0
    tämänhetkinen_nopeus = 0
    kuljettu_matka = 0
    
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus


Possu = Auto('ABC-123', 142)


print(f'Rekisteritunnus: {Possu.rekisteritunnus}\nHuippunopeus: {Possu.huippunopeus}\nTämänhetkinen nopeus: {Possu.tämänhetkinen_nopeus} \nKuljettu matka: {Possu.kuljettu_matka}')










