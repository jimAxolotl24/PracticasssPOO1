from math import pi,tan,sqrt
class Figura():
    def __init__(self,lado,numL):
        self.lado = lado
        self.numL = numL
    
    def calcApotema(self):
            # deben ser minimo 3 lados
            l = self.lado
            nl = self.numL                                 
            apotema = (1/2) * l * tan(pi * (1/2 - 1/nl))
            return apotema
        
    def calcPerimetro(self):
        l = self.lado
        nl = self.numL 
        perimetro = l * nl        
        return perimetro

    def calcArea(self):
        apotema = self.calcApotema()        
        area = self.calcPerimetro() * apotema / 2
        return area
    
l = int(input("MEDIDA DEL LADO -> "))
nl = int(input("NUMERO DE LADOS -> "))

fig1 = Figura(l,nl)

print(f"AREA: {fig1.calcArea():.2f}") 
print(f"PERIMETRO: {fig1.calcPerimetro()}")
        
        
        
