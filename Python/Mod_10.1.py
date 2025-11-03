class Hissi:
    alinkerros = 1
    ylinkerros = 10
    hissin_kerros = 1
    
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros

    
    def kerros_ylös(self):
        if self.hissin_kerros < self.ylinkerros:
            self.hissin_kerros += 1
        print(f'Hissi on kerroksessa: {self.hissin_kerros}')
        return self.hissin_kerros
        
    
    def kerros_alas(self):
        if self.hissin_kerros > self.alinkerros:
            self.hissin_kerros -= 1
        print(f'Hissi on kerroksessa: {self.hissin_kerros}')
        return self.hissin_kerros
    
    
    def siirry_kerrokseen(self, haluttu_kerros):
        if haluttu_kerros >= self.hissin_kerros:
            while haluttu_kerros != self.hissin_kerros:
                self.kerros_ylös()
        else:
            while haluttu_kerros != self.hissin_kerros:
                self.kerros_alas()
        
        
valmis_hissi = Hissi(1,10)

valmis_hissi.siirry_kerrokseen(7)
valmis_hissi.siirry_kerrokseen(1)