from math import sqrt
class Figura:
    def area(lado,nlados):
        if nlados == 4:
            area = lado * lado
            print("Area del Cuadrado: ",area)
        elif nlados == 3:
            area = lado * lado * sqrt(3) / 4
            print("Area del triángulo: ",area)
        else:
            print("En la práctica 3 está el cálculo de area de poligomo de cualquier numero de lados")
    
    def perimetro(lado,nlados):
        print("PERIMETRO: ",lado * nlados)


Figura.area(5,4)
Figura.perimetro(5,4)

Figura.area(4,3)
Figura.perimetro(4,3)





