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


class Talo:
    alinkerros = 1
    ylinkerros = 2
    hissien_maara = 3
    hissit = []
    
    def __init__(self, alinkerros, ylinkerros, hissien_maara):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros 
        self.hissien_maara = hissien_maara
        for h in range(0, hissien_maara):
            self.hissit.append(Hissi(alinkerros, ylinkerros))
            
    def aja_hissiä(self, hissin_nro, kohde_kerros):
        if hissin_nro <= len(self.hissit) and hissin_nro > 0:
            print(f'Hissi numero {hissin_nro} liikkuu.')
            self.hissit[hissin_nro - 1].siirry_kerrokseen(kohde_kerros)
        else:
            print('Valittua hissiä ei ole olemassa.')
    
    def palohälytys(self):
        print('PALOHÄLYTYS!!!')
        for h in range(0, self.hissien_maara):
            self.aja_hissiä(h + 1, self.alinkerros)
            
            
        
            
        
           

talo = Talo(1,10,3)
talo.aja_hissiä(2,9)
talo.aja_hissiä(1,2)
talo.aja_hissiä(2,7)
talo.aja_hissiä(3,4)
talo.palohälytys()