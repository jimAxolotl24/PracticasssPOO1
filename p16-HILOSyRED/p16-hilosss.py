import threading
import time
print("E J E M P L O - 1")
def tarea(nombre,segundos):
    print(f"I n i c i a n d o  * {nombre} * ...")    
    time.sleep(segundos) # Simula trabajo ¿?
    print(f"-> * {nombre} * c o m p l e t a d a  :3")

# CREACION DE LOS HILOS
hilo1 = threading.Thread(
    target = tarea,
    args = ("Tarea - 1",2)
)
hilo2 = threading.Thread(
    target = tarea,
    args = ("Tarea - 2",1)
)

# Inicio de ejecución de los hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen
hilo1.join()
hilo2.join()

print("\n\nE J E M P L O - 2")
class Hilo(threading.Thread):
    def __init__(self,nombre,intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo

    def run(self):
        print (f"*** El hilo >> {self.nombre} << ha comenzado")
        for i in range(5): 
            print(f"El hilo >> {self.nombre} << se encuentra en iteración {i} ")
            time.sleep (self.intervalo)
        print(f"*** El hilo >> {self.nombre} << ha finalizado")
               

hilito1 = Hilo("hilo1",2)
hilito2 = Hilo("hilo2",4)
hilito1.start()
hilito2.start()
hilito1.join()
hilito2.join()

print("\n\nE J E M P L O - 3 (asyncio)")
import asyncio

async def tarea(nombre):
    print (f"*** {nombre} INICIA")
    await asyncio.sleep(2)
    print (f"***{nombre} TERMINA")

async def main():
    await asyncio.gather (
        tarea("Tarea - 1"),
        tarea("Tarea - 2")
    )

asyncio.run(main())