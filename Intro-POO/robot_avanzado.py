"""
    Clase que contiene los atributos privados y cuyo
    constructor recibe los parametros iniciales.
"""
class Robot:

    def __init__(self, nombre:str,
                 peso:float,
                 km:int):
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

    def __str__(self):
        return " Nombre: " + self.get_nombre()+ " Peso: " + str(self.get_peso())+" Km: " +  str(self.get_km())

    def __eq__(self, otro_robot:object)->bool:  
        return self.get_nombre()== otro_robot.get_nombre() and self.get_peso() == otro_robot.get_peso() and self.get_km() == otro_robot.get_km()
        

        
if __name__ == "__main__":
    
    #nombre = input("Dame nombre: ")
    #peso = float(input("Dame peso:"))
    #km = int(input("Dame kilometraje: "))
    
    #wall_e = Robot("Pepe", 40.0, 80)
    #wall_e = Robot(nombre, peso, km)

    #print("Nombre: " , wall_e.get_nombre())
    #print(wall_e)
    
    #wall_e.set_nombre("Pepe el toro")
    #print("Nombre: " , wall_e.get_nombre())

    robotina = Robot("Lola", 100, 20)
    robox = Robot("Lola", 100, 20)

    print("Son iguales: ", robotina == robox)





    
    
