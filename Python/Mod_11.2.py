class Auto:
    rekisteritunnus = ''
    huippunopeus = 0
    tämänhetkinen_nopeus = 0
    kuljettu_matka = 0
    
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

    

        
class Sähköauto(Auto):
        
    tämänhetkinen_nopeus_telsa = 60
    
    
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti_kWh):
        self.akkukapasiteetti_kWh = akkukapasiteetti_kWh
        super().__init__(rekisteritunnus, huippunopeus)
        
    def kulje_sähkö(self, tuntimäärä):
        self.kuljettu_matka += (self.tämänhetkinen_nopeus_telsa * tuntimäärä)
        
class Polttomoottoriauto(Auto):
    
    tämänhetkinen_nopeus_bensa = 90
    
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        self.tankin_koko = tankin_koko
        super().__init__(rekisteritunnus, huippunopeus)
    
    def kulje_bensa(self, tuntimäärä):
        self.kuljettu_matka += (self.tämänhetkinen_nopeus_bensa * tuntimäärä)
    
   
        
tesla = Sähköauto('ABC-15', 180, 52.5)

lada = Polttomoottoriauto('ACD-123', 165, 32.3)

tesla.kulje_sähkö(3)
print(f'teslan kulkema matka {tesla.kuljettu_matka} KM')

lada.kulje_bensa(3)
print(f'Ladan kulkema matka: {lada.kuljettu_matka} KM')