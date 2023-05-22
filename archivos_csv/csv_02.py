from abc import ABC, abstractmethod
from datetime import datetime

class Estudiante:
    def __init__(self, nombre, edad, fecha):
        self.__id_est = 0
        self.__nombre = nombre
        self.__edad = edad
        self.__fecha = fecha

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad =  edad
    
    def get_fecha(self):
        return self.__fecha

    def set_fecha(self,fecha):
        self.__fecha =  fecha

        
    def get_id(self):
        return self.__id_est

    def set_id(self, id_nuevo):
        self.__id_est =  id_nuevo

    def __str__(self):
        return str(self.__id_est)+","+self.__nombre+","+ str(self.__edad) + ","+self.__fecha.strftime('%Y-%m-%d')

    
class ManejadorArchivo(ABC):
    
    @abstractmethod
    def agregar_estudiante(self,estudiante):
        pass
    @abstractmethod
    def buscar_estudiante_id(self,id_est):
        pass
    @abstractmethod
    def modificar_estudiante(self,id_est,nuevo_EST):
        pass
    @abstractmethod
    def eliminar_estudiante(self,id_est):
        pass


class ArchivoEstudiantes(ManejadorArchivo):

    def __init__(self, ruta_archivo):
        self.__ruta_archivo = ruta_archivo
        self.__estudiantes = []

    def leer_archivo(self):
        try:
            count = 0
            with open(self.__ruta_archivo,'r',encoding = 'utf-8') as f:
                 for line in f:
                    data =  line.split(',')
                    id_est = data[0]
                    nombre = data[1] +","+ data[2] +"," +data[3]
                    edad = data[4]
                    date = data[5]
                    date_obj =  datetime.fromisoformat(date.replace("\n",""))
                    
                    estudiante_obj = Estudiante(nombre,edad,date_obj)
                    estudiante_obj.set_id(count)
                    count+=1
                    print(estudiante_obj)
                    self.__estudiantes.append(estudiante_obj)
        except FileNotFoundError:
            print("Archivo no encontrado")

    def escribir_archivo(self):
           try:
                with open(self.__ruta_archivo,'w',encoding = 'utf-8') as f:
                    for est in self.__estudiantes:
                        print(est)
                        f.write(est.__str__()+"\n")
           except FileNotFoundError:
                print("Archivo no encontrado")

    def agregar_estudiante(self,estudiante):
        tam = len(self.__estudiantes)
        estudiante.set_id(tam+1)
        self.__estudiantes.append(estudiante)
        
    def buscar_estudiante_id(self,id_est):
        for est in self._estudiantes:
            if (est.get_id()==id_est):
                return est
        return None
        
    def modificar_estudiante(self,id_est, nuevo_est):
        for est in self.__estudiantes:
            if (est.get_id()==id_est):
                self.__estudiantes[id_est] = nuevo_est
               
    def eliminar_estudiante(self,id_est):
        for est in self.__estudiantes:
            if (est.get_id()==id_est):
                del self.__estudiantes[id_est]
            

                 
                 

archivo = ArchivoEstudiantes("estudiantes_info.csv")
archivo.leer_archivo()
est1= Estudiante("Elsa,Pato,Roto",29,datetime.today())
est2= Estudiante("Rosa,Pato,Roto",28,datetime.today())
est3= Estudiante("Diana,Pato,Roto",27,datetime.today())
est4= Estudiante("Lola,Pato,Roto",26,datetime.today())
archivo.agregar_estudiante(est1)
archivo.agregar_estudiante(est2)
archivo.agregar_estudiante(est3)
archivo.agregar_estudiante(est4)

archivo.eliminar_estudiante(1)
est5= Estudiante("Sergio,Molotla,Molotla",27,datetime.today())
archivo.modificar_estudiante(0,est5);

archivo.leer_archivo()

archivo.escribir_archivo()


    
