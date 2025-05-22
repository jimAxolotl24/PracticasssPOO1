'''27 - Marzo - 2025. EJERCICIO: Crear lista de 5 valores mixtos y una lista de 5 valores del mismo tipo, convertirlas a tupla
y conjuntos. Crear un dicionario de 5 elementos con valotes de distinto tipo'''

import numpy as np
from numpy import array

listita1 = [1,"si",12.5,False,1]

listita2 = np.array(["abc","bc","abc","ab","ac"])

tupl1 = tuple(listita1)
tupl2 = tuple(listita2)

setl1 = set(listita1)
setl2 = set(map(str,listita2))

dicc1 = {"producto":"Frapuccino","sabor":"Moka","precio":30.75,"tamaños":["CH","M","G"],"cantidad":37}

print("LISTAS:")
print("-> ",listita1)
print("-> ",listita2)

print("LISTAS CONVERTIDAS A TÚPLA:")
print("-> ", tupl1)
print("-> ", tupl2)

print("LISTAS CONVERTIDAS A CONJUNTO:")
print("-> ", setl1)
print("-> ", setl2)

print("DICCIONARIO:")
for k,v in dicc1.items():
    print(f"-> {k} : {v}")
 
# PRACTIQUITA USO SETS
print("\n\nU S O  D E  S E T S")
conjuntito = {1,2,4,8,16}
print("CONJUNTO: ",conjuntito)
conjuntito.add(32)
print("*** Agregar nuevo valor > 32 < ",conjuntito)
conjuntito.remove(8)
print("*** Quitar el > 8 < :",conjuntito)
# conjuntito.remove(25) da error
conjuntito.discard(25) # este no da error

print("*** ¿5 está en el conjunto?: ",5 in conjuntito)
conjuntito.add(16)
print("*** Agregar repetido > 16 <: ",conjuntito," no cambia nada")

# Union: A.union(B) A | B
# Intersección: A.intersection(B) A & B
# Diferencia: A.difference(B) A - B
# Diferencia Simétrica: A.symmetric:difference(B) A ^ B 
# Es Subconjunto: A.issubset(B)
# Es ¿Superconjunto?: B.issuperset(A)
# Contar Elementos: len(A)
# Vaciar Conjunto: clear()
# A.copy() <-
# No comparten elementos -> A.isdisjoint(B)

# PRACTIQUITA USO DICCIONATRIOS
print("\n\nU S O  D E  D I C C I O N A R I O S")
d1 = {"1":"uno","2":"dos","3":"tres"}
d2 = dict(x="equis",y="ye",z="zeta")

print(d1["1"]) # debe existir el elemento
print(d1.get("3"))
print(d1.get("5"))


d1["4"] = "cuatro" # agregar elementos

# Eliminar elementos
print("eliminar > 2 <")
x = d1.pop("2")
print(d1)

llaves = d1.keys()
print(llaves)

valores = d1.values()
print(valores)

p = d1.items()
print(p)

print(d1.get("1","uno"))
# d1.clear()
# d1.update(?)'''