# -*- coding: utf-8 -*-
"""

@author: guest
"""

import csv

from abc import ABC, abstractmethod

from Pregunta import Pregunta

class GestorArchivosAbstract(ABC):

    @abstractmethod
    def leer_archivo(self, archivo:str):
        pass

    @abstractmethod
    def escribir_archivo(self, archivo:str, datos:list):
        pass



class ArchivoCSV():
    
    def __init__(self, nombre_archivo: str):
        self.__nombre_archivo =  nombre_archivo
    
    def leer_csv(self):
        preguntas = []
        try:
            with open(self.__nombre_archivo, 'r') as archivo:
                lector_csv = csv.reader(archivo)
                for linea in lector_csv:
                    # Suponiendo que cada línea contiene la información de una pregunta en un formato específico
                    # Puedes adaptar esta parte según la estructura del archivo CSV y la clase Pregunta
                    tipo = linea[0]
                    descripcion = linea[1]
                    respuestas = linea[2:]
    
                    pregunta = Pregunta(tipo, descripcion)
                    pregunta.agregar_respuesta(respuestas)
    
                    preguntas.append(pregunta)
        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
             print("Error al leer el archivo:", str(e))
        return preguntas

    def escribir_csv(self, datos):
        print("Se van a guardar...")
        try:
            with open(self.__nombre_archivo, 'w', newline='') as archivo_csv:
                for elemento in datos:
                    archivo_csv.write(elemento.__str__())
        except (PermissionError, TypeError) as e:
            print("Error al escribir en el archivo:", str(e))




