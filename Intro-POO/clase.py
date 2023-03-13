class Alumno:
	def __init__(self, nombre, apellidoPaterno, apellidoMaterno):
		self.__nombre = nombre
		self.__apellidoPaterno= apellidoPaterno
		self.__apellidoMaterno = apellidoMaterno
        

alumnoDiego = Alumno("Diego","Vera","Juárez")

print(alumnoDiego.nombre)