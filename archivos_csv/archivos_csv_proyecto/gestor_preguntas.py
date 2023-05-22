# -*- coding: utf-8 -*-
"""


@author: guest
"""


import csv
from abc import ABC, abstractmethod
from gestor_archivos import GestorArchivosAbstract

class ManejadorPreguntasAbstract(ABC):
    
    @abstractmethod
    def agregar_pregunta(self,pregunta):
        pass
    
    @abstractmethod
    def leer_todas_pregunta(self):
        pass
    
    @abstractmethod
    def guardar_preguntas(self, datos):
        pass

    @abstractmethod
    def modificar_pregunta(self, indice, nueva_pregunta):
        pass

    @abstractmethod
    def borrar_pregunta(self, indice):
        pass
    

class ManejadorPreguntas(ManejadorPreguntasAbstract):
    
     def __init__(self, manejador_archivos):
        self.__lista_preguntas = []
        self.__manejador_archivos = manejador_archivos
    
     def agregar_pregunta(self, pregunta):
         self.__lista_preguntas.append(pregunta)

     def leer_todas_pregunta(self):
         self.__manejador_archivos.leer_csv()
     
     def guardar_preguntas(self):
         self.__manejador_archivos.escribir_csv(self.__lista_preguntas)

     def modificar_pregunta(self, indice, nueva_pregunta):
         if 0 <= indice < len(self.__lista_preguntas):
             self.__lista_preguntas[indice] = nueva_pregunta
         else:
             raise ValueError ('El índice de la pregunta no es válido')
             
     def borrar_pregunta(self, indice):
         if 0 <= indice < len(self.__lista_preguntas):
             del self.__lista_preguntas[indice]
         else:
             raise ValueError ('El índice de la pregunta no es válido')
             
    
    
    
    