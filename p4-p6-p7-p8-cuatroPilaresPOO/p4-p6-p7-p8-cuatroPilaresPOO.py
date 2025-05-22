# EJEMPLOS DE LOS 4 PILARES DE POO
print("E N C A P S U L A M I E N T O")

class CuentaBancaria:
    def __init__(self,saldo_inicial,numCuenta):
        self.__saldo = saldo_inicial # atributo privado
        self.__numCuenta = numCuenta
    
    def depositar(self,cantidad):
        self.__saldo += cantidad
        print(f"* Se depositaron ${cantidad}. Saldo actual: ${self.__saldo}")
    
    def retirar(self,cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            print(f"* Se retiraron ${cantidad}. Saldo actual: ${self.__saldo}")
        else:
            print("saldo insuficiente")


cuenta1 = CuentaBancaria(5000,123454321)
cuenta1.retirar(2500)
cuenta1.depositar(3000)


# 2 - HERENCIA
print("\n\nH E R E N C I A")
print("\n*** Ejemplo - 1 ***")
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        return "* sonido gnerico *"
        
    def presentarse(self):
        return f"Hola me llamo {self.nombre} y tengo {self.edad} años c:"
    
class Perro(Animal):  # Perro hereda de Animal
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase padre
        self.raza = raza
    
    def hacer_sonido(self):  # Sobrescribe el método de la clase padre
        return "¡Guau! ¡Guau!"
        
    def presentarse(self):
        return super().presentarse() + f" y soy un perro de raza {self.raza}"


# creacion de los objetos
mi_perro = Perro("Roco", 3, "Pastor Alemán")
print(mi_perro.presentarse())  
print(mi_perro.hacer_sonido())  

print("\n*** Ejemplo - 2 ***")
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def informacion(self):
        return f"Vehículo {self.marca} {self.modelo}"
    
class Electrico:
    def __init__(self, autonomia):
        self.autonomia = autonomia
    def cargar(self):
        return "Cargando batería..."

class CocheElectrico(Vehiculo, Electrico):
    def __init__(self, marca, modelo, autonomia):
        Vehiculo.__init__(self, marca, modelo)
        Electrico.__init__(self, autonomia)
    
    def informacion(self):
        return f"{Vehiculo.informacion(self)} - Autonomía: {self.autonomia} km"

# creacion de los objetos
tesla = CocheElectrico("Tesla", "Model 3", 500)
print(tesla.informacion())
print(tesla.cargar())

# 3- POLIMORFISMO
print("\n\nP O L I M O R F I S M O")

class Forma:
    def dibujar(self):
        return "* Dibujando una forma* "
    
    def area(self):
        return "* Calcular area de Figura *"
    
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def dibujar(self):  
        return "* Dibujando un círculo *"
    
    def area(self):   
        return 3.14159 * self.radio * self.radio
    

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def dibujar(self): 
        return "* Dibujando un rectángulo *"
    
    def area(self):
        return self.ancho * self.alto
 
def procesar_forma(forma):
    print(forma.dibujar())
    print(f"Area: {forma.area()}")
 
procesar_forma(Circulo(5))
procesar_forma(Rectangulo(4, 6))

print("\n\nA B S T R A C C I O N")

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Método concreto (con implementación)
    def respirar(self):
        print(f"{self.nombre} está respirando...")
    
    # Método abstracto (sin implementación)
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    # Otro método abstracto
    @abstractmethod
    def moverse(self):
        pass
class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    # Implementación del método abstracto
    def hacer_sonido(self):
        return "Los odio a todos digo, miau"
    
    # Implementación del método abstracto
    def moverse(self):
        print(f"{self.nombre} * corre en cuatro patas *")


# animal = Animal("Genérico")  # Error: No se puede instanciar una clase abstracta
gatito = Gato("Milaneso", "Egipcio")
gatito.respirar()
print(gatito.hacer_sonido())
gatito.moverse()