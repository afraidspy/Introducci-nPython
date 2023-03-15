"""
    Clase que contiene los atributos privados y cuyo
    constructor recibe los parametros iniciales.
"""
class Robot:

    def __init__(self, nombre:str, peso:float, km:int):
        self.__nombre = nombre
        self.__peso = peso
        self.__km = km

    def get_nombre(self)-> str:
        return self.__nombre

    def set_nombre(self,nuevo_nombre:str):
        self.__nombre = nuevo_nombre

    def get_peso(self)->float:
        return self.__peso

    def set_peso(self, nuevo_peso:float):
        #self.__peso = nuevo_peso
        self.__peso = nuevo_peso if nuevo_peso > 0 else 0 

    def get_km(self)-> int:
        return self.__km

    def set_km(self, km:int):
        #self.__km = km
        self.__km = km if km > 0 else 0

        
if __name__ == "__main__":

    wall_e = Robot("Pepe", 40.0, 80)

    print("Nombre: " , wall_e.get_nombre())

    wall_e.set_nombre("Pepe el toro")
    print("Nombre: " , wall_e.get_nombre())





    
    
