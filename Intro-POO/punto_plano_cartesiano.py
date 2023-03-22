import math
class Punto:
    def __init__(self,x=0, y=0):
        ##Variables de instancia
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x
        
    def set_y(self, y):
        self.__y = y
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def suma(self,otro_punto):
        #print(otro_punto.get_x())
        coord_x = self.__x + otro_punto.get_x()
        coord_y = self.__y + otro_punto.get_y()
        punto_suma = Punto(coord_x, coord_y)
        return punto_suma
        ## return Punto(self.__x + otro_punto.get_x(), self.__y + otro_punto.get_y())

    def resta(self,otro_punto):
        #print(otro_punto.get_x())
        coord_x = self.__x - otro_punto.get_x()
        coord_y = self.__y - otro_punto.get_y()
        punto_resta = Punto(coord_x, coord_y)
        return punto_resta

    def distancia(self, otro_punto):
        val1= (otro_punto.get_x() - self.__x)*(otro_punto.get_x() - self.__x)
        val2 = math.pow((otro_punto.get_y() - self.__y),2)
        sum_val =  val1+val2
        return math.sqrt(sum_val)
        

    def __str__(self):
        return "("+ str(self.__x) + " , " + str(self.__y) + ")"

        


punto1 = Punto(2,2)
punto2 = Punto(2,2)
print("Son iguales: " , punto1 == punto2)
punto3 = punto1.suma(punto2)

print("x",punto3.get_x())
print("y",punto3.get_y())

print(punto3)




