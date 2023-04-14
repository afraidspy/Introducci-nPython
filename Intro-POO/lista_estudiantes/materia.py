class Materia:

    def __init__(self, codigo:float,nombre:float, calif:float):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__calificacion = calif

    #Crear set y get para cada atributo


    #Crear método str
    def __str__(self):
        return "Nombre: " + self.__nombre + " Calif: " + str(self.__calificacion)

    #Agregar método __eq__
    
