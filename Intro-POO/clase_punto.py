"""
Clase para representar punto en el plano cartesiano
Autor: Jessica
"""

class Punto:

    def __init__(self, x = 0:float, y =0:float):
    """
    Constructor de la clase que inicializa
    los atributos x e y de un objeto
    que representa una coordenada
    en un plano cartesiano.
    Params:
          x(float): Coordenada en el eje X. Por defecto es 0
          y(float): Coordenada en el eje Y. Por defecto es 0
    """
        self.__x = x
        self.__y = y


    def set_x(self, x:float):
    """
        Método modificador que permite cambiar el
        valor de la coordenada x
        Params:
            x(float) :  El nuevo valor que se le va asignar a x
    """
        self.__x = x
        
    def set_y(self, y_float):
    """
        Método modificador que permite cambiar el
        valor de la coordenada y
        Params:
            y(float) :  El nuevo valor que se le va asignar a y
    """
        self.__y = y
    
    def get_x(self)->float:
    """
        Método acceso que permite obtener el
        valor de la coordenada x
        Returns:
            float:  Regresa el valor de x
    """
        return self.__x

    def get_y(self) -> float:
    """
        Método acceso que permite obtener el
        valor de la coordenada y
        Returns:
            float:  Regresa el valor de y
    """
        return self.__y


if __name__ == "__main__":

    punto =  Punto()
    punto2 = Punto(4,5)
