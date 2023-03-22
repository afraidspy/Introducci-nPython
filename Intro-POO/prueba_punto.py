"""
Script de prueba
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
        elif opcion == 3:
            print("Distancia")
        elif opcion == 4:
            print("Desplazamiento")





    

