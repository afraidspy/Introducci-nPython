class Robot:
    #método constructores
    def __init__(self):
        """
        Atributos públicos
        self.nombre = "Beto"
        self.edad = 100
        self.num_armas = 0
        self.peso = 200
        self.altura = 2
        """
        #Atributos privados
        self.__nombre = "Beto"
        self.__edad = 100
        self.__num_armas = 0
        self.__peso = 200
        self.__altura = 2
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return sel.__edad
	
	
robot1 = Robot()
#LLamando a las variable pública
"""print(robot1.__nombre)
print(robot1.__edad)
print(robot1.__num_armas)
"""
print(robot1.getNombre())

"""robot2 = Robot()
print(robot2.nombre)"""
