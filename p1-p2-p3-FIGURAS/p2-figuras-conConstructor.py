from math import sqrt
class Figura:
    def __init__(self,lado,nlados):
        self.lado = lado 
        self.nlados = nlados

    def area(self):
        l = self.lado
        nl = self.nlados

        if nl == 4:
            area = l * l
            print("Area del Cuadrado: ",area)
        elif nl == 3:
            area = l * l * sqrt(3) / 4
            print("Area del triángulo: ",area)
        else:
            print("En la práctica 3 está el cálculo de area de poligomo de cualquier numero de lados")
    
    def perimetro(self):
        l = self.lado
        nl = self.nlados

        print("PERIMETRO: ",l * nl)

fig1 = Figura(5,4)
fig1.area()
fig1.perimetro()

fig2 = Figura(4,3)
fig2.area()
fig2.perimetro()





