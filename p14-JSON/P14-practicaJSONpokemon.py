import json
import requests

class GestorJson:
    def __init__(self,arch):
        self.arch = arch
        
    def leerJson(self):
        try:
            with open(self.arch,'r') as f:
                return json.load(f)
            
        except FileNotFoundError:
            print("Archivo no existe :c")
            return {}
        
        except json.JSONDecoderError:
            print("El archivo no es JSON :^")
    
    def escribirJson(self,datos):
        with open(self.arch,'w') as f:
            return json.dump(datos,f,indent = 4)
        
    def modificarJson(self,llave,valor):
        datos = self.leerJson()
        datos[llave] = valor
        self.escribirJson(datos)
        
    def obtenerPokemon(self,pokemon):
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.escribirJson(data)
        except requests.exceptions.HTTPError:
            print("El enlace no existe :c")
        except requests.exceptions.RequestException:
            print("No se pudo realizar la petición pipipi")

# creacion del objetito 
gjson = GestorJson("pokemon.json")
gjson.obtenerPokemon("Pikachu")

# MODIFICAR EL JSON
gjson.modificarJson("cries","PIPIPI")

# pokemonInfo = gjson.leerJson()
# print(pokemonInfo)
        
        
