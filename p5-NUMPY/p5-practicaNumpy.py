import numpy as np

class Lista:
    def __init__(self):        
        self.arregloList = []

    def insertar(self,valor):
        print(f"-> Se insertó el elemento {valor} en la lista")
        self.arregloList.append(valor)               
        print(self.arregloList)

    def eliminar(self,posc):
        if posc <= len(self.arregloList):
            print(f"-> Se eliminó el elemento en la posición {posc} de la lista")
            self.arregloList.pop(posc)            
            print(self.arregloList)

    def modificar(self,posc,valor):
        if posc <= len(self.arregloList):
            print(f"-> Valor del elemento en la posición {posc} de la lista cambiado a {valor}")
            self.arregloList[posc] = valor     
            print(self.arregloList)   
  
    def mostrar(self):
        print("LISTA:")
        print(self.arregloList)

        
class ArregloNP:
    def __init__(self,u):
        self.arreglitoNP = np.zeros(u) 
        # porque quiero mi arreglo de dimnsion "u" y no un arreglo con un elemento "u" :^
        
    def insertarNP(self,posc,valor):
        if posc <= self.arreglitoNP.size:
            print(f"-> Se insertó el elemento {valor} en la posición {posc} del arreglo")
            self.arreglitoNP = np.insert(self.arreglitoNP,posc,valor)
            print(self.arreglitoNP)
    
    def eliminarNP(self,posc):
        print(f"-> Se eliminó el elemento en la posición {posc} del arreglo")
        self.arreglitoNP = np.delete(self.arreglitoNP,posc)
        print(self.arreglitoNP)

    def modificarNP(self,posc,valor):
        print(f"-> Valor del elemento en la posición {posc} de arreglo cambiado a  {valor}")
        self.arreglitoNP[posc] = valor
        print(self.arreglitoNP)
        
    def mostrarNP(self):
        print("ARREGLO:")
        print(self.arreglitoNP)
        
# LISTA
listita = Lista()

print("* * * * * * * * LISTA INICIAL * * * * * * * *")
listita.mostrar()
print("\n* * * * * * * * INSERTAR ELEMENTOS * * * * * * * *")
for i in range(5):
    listita.insertar((i+1))
print("\n* * * * * * * * MODIFICAR ELEMENTO * * * * * * * *")
listita.modificar(3,10)
print("\n* * * * * * * * ELIMINAR ELEMENTO * * * * * * * *")
listita.eliminar(2)


# ARREGLO NUMPY
arreglo = ArregloNP(5)

print("\n\n\n* * * * * * * * ARREGLO INICIAL * * * * * * * *")
arreglo.mostrarNP()
print("\n* * * * * * * * MODIFICAR ELEMENTO * * * * * * * *")
for i in range(5):
    arreglo.modificarNP(i,(i+1))
print("\n* * * * * * * * ELIMINAR ELEMENTO * * * * * * * *")
arreglo.eliminarNP(2)
print("\n* * * * * * * * INSERTAR ELEMENTOS * * * * * * * *")
arreglo.insertarNP(1,17)
arreglo.insertarNP(3,35)
