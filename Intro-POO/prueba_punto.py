"""
    Script de prueba
    Autor: Jessica
"""

from clase_punto import Punto


if __name__ == "__main__":

    punto =  Punto()
    punto2 = Punto(4,5)


    while(True):
        print(" \n[0] Salir"+
           "\n[1] Resta  " +
           "\n[2] Suma "+
           "\n[3] Distancia"+
           "\n[4] Desplazamiento")      
        opcion = int(input("Escribe una opción:"))
        if opcion == 0:
            print("Fin del programa")
            break
        elif opcion == 1:
            print("Resta")
            x1 = float(input("Dame primer coordenada: "))
            y1 = float(input("Dame segunda coordenada: "))
            punto1 =  Punto(x1,y1)
            x2 = float(input("Dame primer coordenada: "))
            y2 = float(input("Dame segunda coordenada: "))
            punto2 =  Punto(x2,y2)

            punto_resta = punto1.resta(punto2)

            print("Resta: ",punto_resta) 
        elif opcion == 2:
            print("Suma")
            x1 = float(input("Dame primer coordenada: "))
            y1 = float(input("Dame segunda coordenada: "))
            punto1 =  Punto(x1,y1)
            x2 = float(input("Dame primer coordenada: "))
            y2 = float(input("Dame segunda coordenada: "))
            punto2 =  Punto(x2,y2)

            punto_suma = punto1.suma(punto2)

            print("Suma: ",punto_suma) 

        elif opcion == 3:
            print("Distancia")
            x1 = float(input("Dame primer coordenada: "))
            y1 = float(input("Dame segunda coordenada: "))
            punto1 =  Punto(x1,y1)
            x2 = float(input("Dame primer coordenada: "))
            y2 = float(input("Dame segunda coordenada: "))
            punto2 =  Punto(x2,y2)

            resultado_distancia = punto1.distancia(punto2)

            print("Resultado: ", resultado_distancia)
            
        elif opcion == 4:
            print("Desplazamiento")

            x1 = float(input("Dame primer coordenada: "))
            y1 = float(input("Dame segunda coordenada: "))
            punto1 =  Punto(x1,y1)

            despl_x = input("Escribe el desplazamiento en x: ")
            despl_y = input("Escribe el desplazamiento en y: ")

            punto_nuevo = punto1.desplazamiento(despl_x, despl_y)
            
        else:
            print("Escribe una opción válida")






    

