# -*- coding: utf-8 -*-
"""
"""
from Respuesta import Respuesta

from abc import ABC, abstractmethod


from abc import ABC, abstractmethod

class AbstractPregunta(ABC):
    
    @abstractmethod
    def agregar_respuesta(self, respuestas):
        pass



class Pregunta(AbstractPregunta):
    def __init__(self,tipo, descripcion):
        self.__tipo =  tipo
        self.__descripcion = descripcion
        self.__respuestas = []

    def agregar_respuesta(self, respuestas):
        self.__respuestas = respuestas
        print("Respuesta...")
        print(self.__respuestas)
        

    
    def __str__(self):
        datos = [self.__tipo, self.__descripcion]
        respuesta_str = ', '.join(str(respuesta) for respuesta in self.__respuestas)
        return ', '.join(str(dato) for dato in datos) + ', ' + respuesta_str
