class Robot2:
	def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso
    
    def getNombre(self):
        return self.__nombre

robotina = Robot("Robotina","10")
robocob = Robot("Robocob","150")

print("Nombre del primer Robot " + robotina.getNombre())

print("Nombre del segundo Robot " + robocob.getNombre())