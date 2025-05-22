class Patron:
    def traerCheve(self):
        pass

class Morra:
    def traerCheve(self):
        return "Yo si traigo y pago cheves por ser buchona y empoderada ajua"

class Pisto:
    def __init__(self,hielera,hielera2):
        self.__hielera = hielera
        self.hielera2 = hielera2
    
    def pistear(self):
        self.__hielera = "* * * v a c i a r * * *"
        return self.__hielera
        
    def pistear2(self):
        self.hielera2 = "Nah. Está vacía"
        return self.hielera2
        
fiesta = Pisto("Cartón en hielera","Unas cuantas frias")

print(fiesta.pistear())
print(fiesta.pistear2()) 



