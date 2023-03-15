"""
    Ejemplo de una clase que contiene sus atributos privados
    Autor: Jessica
"""
class Robot:
    def __init__(self):
        self.__nombre = "Beto"
        self.__peso = 300.0
        self.__km = 100
        
    def get_nombre(self)-> str:
        return self.__nombre

    def set_nombre(self,nuevo_nombre:str):
        self.__nombre = nuevo_nombre

    def get_peso(self)->float:
        return self.__peso

    def set_peso(self, nuevo_peso:float):
        self.__peso = nuevo_peso

    def get_km(self)-> int:
        return self.__km

    def set_km(self, km:int):
        self.__km = km
        

if __name__ == "__main__":

    robocob = Robot()

    print("Nombre: ", robocob.get_nombre())

    robocob.set_nombre("Bad bunny")

    print("Nombre: ", robocob.get_nombre())

    print("Peso: " ,robocob.get_peso())

    robocob.set_peso(50.0)
    
    print("Peso: " ,robocob.get_peso())

    print("Km: " ,robocob.get_km())
    
    robocob.set_km(2000)

    print("Km: " ,robocob.get_km())




    

    #print(robocob.__nombre)
