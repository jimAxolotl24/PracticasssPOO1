from typing import Final
from enum import Enum

# UN EJMPLITO INCOMPLETO ¿¿¿???
'''
class Usuario:
    Max_usuario: Final = 1000

    try:
        a = (3/0)
        print(a)
    except ZeroDivisionError:
        print("No sirve :^")
    finally: 
        print("Error desconocido :(")
'''

# DIAS DE LA SEMANA CON ENUM
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
            raise ValueError(f"El día <{dia}> no es válido. Debe ser un dia de la semana")

    except TypeError as e:
        print(f"Error de tipo: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("* * * EJECUCION FINALIZADA * * *\n")

Verificador("Lunes")
Verificador("domingo")
Verificador("Navidad")
Verificador(7)