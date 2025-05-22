from enum import Enum

lunes = 1
martes = 2
miercoles = 3

class consecutivo(Enum):
    lunes = 1
    martes = 2
    miercoles = 3
    

print(consecutivo.lunes,"\n")
print("TIPO: ",type(consecutivo.lunes))
print(consecutivo.lunes.value)
print("TIPO: ",type(consecutivo.lunes.value))
print(consecutivo.lunes.name)
print("TIPO: ",type(consecutivo.lunes.name))

'''raise exception("") para poner ecxepciones sin usar el nombre???

from typing import Final
from enum import Enum

class Dias(Enum):
    lunes = "Lunes"
    martes = "Martes"
    miercoles = "Miercoles"
    jueves = "Jueves"
    viernes = "Viernes"
    sabado = "Sábado"
    domingo = "Domingo"


def Verificador(dia):
    # def __init__(self,dia:Dias):
    #     self.dia = dia
    try:
        if not isinstance(dia,str):
            raise TypeError("Se esperaba un valor de tipo String :(")

        dia = dia.capitalize() #normalizar el formato ???

        if dia in {d.value for d in Dias}:
            print(f"Dia válido: {dia}")
        else:
            raise ValueError("El día <{dia}> no es válido. Debe ser un dia de la semana")

    except TypeError as e:
        print(f"Error de tipo: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("* * * EJECUCION FINALIZADA * * *\n")

Verificador("Lunes")
Verificador("domingo")
Verificador("Navidad")
Verificador(2025)'''