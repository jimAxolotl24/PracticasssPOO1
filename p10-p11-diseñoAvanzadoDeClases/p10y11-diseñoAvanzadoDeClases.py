from abc import ABC, abstractmethod
class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    @abstractmethod
    def obtenerVelocidadMaxima(self):
        pass

# Interfaces Conducible  y Mantenible
class Conducible(ABC):
    @abstractmethod
    def conducir(self):
        pass

    @abstractmethod
    def estacionar(self):
        pass

class Mantenible(ABC):
    @abstractmethod
    def revisar(self):
        pass

    @abstractmethod
    def reparar(self):
        pass

# clases Coche, Bicicleta, Motocicleta

class Coche(Vehiculo,Conducible,Mantenible):
    def mover(self):
        print("Coche: * moverse *")

    def detener(self):
        print("Coche: * detenerse *")

    def obtenerVelocidadMaxima(self):
        return 180
    
    def conducir(self):
        print("Conduciendo el coche ...")
    def estacionar(self):
        print("Estacionando el coche ...")

    def revisar(self):
        print("> Revisando el coche <")

    def reparar(self):
        print("> Reparando el coche <")


class Motocicleta(Vehiculo,Conducible,Mantenible):
    def mover(self):
        print("Moto: * moverse *")

    def detener(self):
        print("Moto: * detenerse *")

    def obtenerVelocidadMaxima(self):
        return 160
    
    def conducir(self):
        print("Conduciendo la moto ...")
    def estacionar(self):
        print("Estacionando la moto ...")

    def revisar(self):
        print("> Revisando la moto <")

    def reparar(self):
        print("> Reparando la moto <")


class Bicicleta(Vehiculo,Conducible):
    def mover(self):
        print("Bicicleta: * avanza *")

    def detener(self):
        print("Bicicleta: * detenerse *")

    def obtenerVelocidadMaxima(self):
        return 30
    
    def conducir(self):
        print("Pedaleando la bicicleta ...")

    def estacionar(self):
        print("Apoyando la bicicleta sobre la pared ...")


def operarVehiculo(vehiculo: Vehiculo):
    print("o - o - o - o - o - o - o - o - o - o - o - o - o - o")
    vehiculo.mover()
    vehiculo.detener()
    print(f">>> VELOCIDAD MAXIMA: {vehiculo.obtenerVelocidadMaxima()} <<<")
    if isinstance(vehiculo,Conducible):
        vehiculo.conducir()
        vehiculo.estacionar()
    if isinstance(vehiculo,Mantenible):
        vehiculo.revisar()
        vehiculo.reparar()
    print("o - o - o - o - o - o - o - o - o - o - o - o - o - o\n")

vehiculosss = [Coche(),Motocicleta(),Bicicleta()]

for v in vehiculosss:
    operarVehiculo(v)