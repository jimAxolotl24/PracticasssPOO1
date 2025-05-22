import threading
import time

print("\n\nE J E M P L O - 2")
class Hilo(threading.Thread):
    def __init__(self,nombre,intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo

    def run(self):
        print (f"*** El hilo >> {self.nombre} << ha comenzado")
        for i in range(5): 
            print(f"El hilo >> {self.nombre} << se encuentra en iteración {i+1} ")
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