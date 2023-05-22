class Estudiante:
    def __init__(self, nombre, edad, fecha):
        self.__nombre = nombre
        self.__edad = edad
        self.__fecha = fecha

    def get_nombre(self, nombre):
        return self.__nombre

    def set_nombre(self, nombre):
        return self.__nombre

    def get_edad(self, nombre):
        return self.__edad

    def set_edad(self, nombre):
        return self.__edad
    
    def get_fecha(self, nombre):
        return self.__nombre

    def set_fecha(self, nombre):
        return self.__nombre

    def __str__(self):
        return nombre + " , " + str(edad) + " " + fecha

from abc import ABC, abstractmethod
#interface --> clase abstracta donde todos los métodos abstracta
class ManejadorArchivo(ABC):
    @abstractmethod
    def agregar_estudiante(self,estudiante):
        pass
    @abstractmethod
    def buscar_estudiante_date(self,id_est):
        pass
    @abstractmethod
    def modificar_estudiante(self,id_est):
        pass
    @abstractmethod
    def eliminar_estudiante(self,id_est):
        pass



class EstudiantesInfo(ManejadorArchivo):

    def __init__(self,ruta_archivo):
        self.__file_csv =  ruta_archivo
        self.__list_student = []

    def agregar_estudiante(self,estudiante):
        self.__list_student.append(estudiante)
        
    
    def buscar_estudiante_date(self,id_est):
        
    
    def modificar_estudiante(self,id_est):
        
    
    def eliminar_estudiante(self,id_est):
        pass
    
