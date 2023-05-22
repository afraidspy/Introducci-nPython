# -*- coding: utf-8 -*-
"""
@author: guest
"""
class Respuesta:
    def __init__(self, descripcion, es_correcta):
        self.__descripcion = descripcion
        self.__es_correcta = es_correcta

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_es_correcta(self):
        return self.__es_correcta

    def set_es_correcta(self, es_correcta):
        self.__es_correcta = es_correcta

    def __str__(self):
        return self.__descripcion + ", " + str(self.__es_correcta)
