
from punto import Punto
from abc import ABC, abstractmethod

class ObjetoEspacial(ABC):

    def __init__(self, nombre, punto):
        self.nombre = nombre
        self.origen = punto
        
    @abstractmethod
    def mover(self, nuevo):
        self.origen = nuevo

    @abstractmethod
    def dibujar(self):
        pass


class Nave(ObjetoEspacial):

    def __init__(self, nombre, punto):
        super().__init__(nombre,punto)

    def dibujar(self):
        print("Dibjando nave ...")


class Ovni(ObjetoEspacial):

    def __init__(self, nombre, punto):
        super().__init__(nombre, punto)

    def dibujar(self):
        print("Dibjando ovni ...")
        

    
        



objeto = ObjetoEspacial("planeta", Punto(2,8))
nave = Nave("Nave1",Punto(2,3))
nave.mover(Punto())
nave.dibujar()

ovni = Ovni("Ovni1", Punto())
ovni.dibujar()
