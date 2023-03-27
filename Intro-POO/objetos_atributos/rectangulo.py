
from clase_punto import Punto

class Rectangulo:

    def __init__(self, centro=Punto(),ancho=10.0, alto=10.0):
        self.__centro = centro
        self.__ancho = abs(ancho) if ancho < 0 else ancho
        self.__alto = abs(alto) if alto < 0 else alto

    def desplazar(self, aumento_x:float, aumento_y:float):
        self.__centro.desplazamiento(aumento_x, aumento_y)

    def perimetro(self)->float:
        return self.__ancho*2 + self.__alto*2

    def area(self)->float:
        return self.__ancho* self.__alto

    def tipo(self):
        if (self.__ancho == self.__alto):
            return "Cuadrado"
        else:
            return "Rectangulo"
        #return "Cuadrado" if self.__ancho == self.__alto else "Rectangulo"

    def __str__(self):
        return self.__centro.__str__()+ "alto: " + str(self.__alto) + "ancho: " + str(self.__ancho)


if __name__ == "__main__":
    rect1 = Rectangulo()
    print(rect1)
    punto_inicio = Punto(8,8)
    rect2 = Rectangulo(punto_inicio, 20,15)
    print(rect2)
    rect3 = Rectangulo(punto_inicio,-3,-5)
    print(rect3)



    

