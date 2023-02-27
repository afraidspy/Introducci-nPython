'''
    Programa para simular el juego de piedra, papel o tijera
    PIEDRA = 1
    PAPEL  = 2
    TIJERA = 3

    USUARIO  COMPU
    PIEDRA   PAPEL   ---> Gana el usuario
    PAPEL    TIJERA  ---> Gana el usuario
    TIJERA   PIEDRA  ---> Gana el usuario

    PAPEL    PIEDRA  ---> Gana  la compu
    TIJERA   PAPEL   ---> Gana  la compu
    PIEDRA   TIJERA  ---> Gana  la compu
    Objetivo: Hacer uso del if en el juego "piedra, papel o tijera"
'''
#Se importa el módulo random, el cuál permite generar números aleatorios
#Un módulo es un archivo con extensión .py el cuál contiene diversas funciones
#https://docs.python.org/es/3/library/random.html
import random

if __name__ == '__main__':

    #La función randrage(a,b) genera un número aleatorio
    #que se encuentra en el intervalo [a,b) = [a, b-1]
    aleatorio =  random.randrange(1,4) #[1,4) = [1,3]
    print(aleatorio)

    #Declaración de variables
    mi_opcion = 0
    mi_arma = ''
    arma_compu = ''

    #Asingar el arma según la opción escrita por el usuario

    print("Escribe 1 para elegir piedra, 2 para elegir papel y 3 para elegir tijera: ")
    #mi_opcion = input()
    #faltó convertir mi_opcion a un número entero , usando la función int()
    mi_opcion = int(input())
    

    if mi_opcion == 1:
        mi_arma = 'piedra'
    elif mi_opcion == 2:
        mi_arma = 'papel'
    elif mi_opcion == 3:
        mi_arma = 'tijera'
    else:
        print('El número escrito no es válido')

    #Asignar el arma según la opción elegida por la compu

    if aleatorio == 1:
        arma_compu = 'piedra'
    elif aleatorio == 2:
        arma_compu = 'papel'
    elif aleatorio == 3:
        arma_compu = 'tijera'

    #Imprimir el valor de las armas ,tanto de la compu cómo del usuario
    print('El arma del usuario es', mi_arma)
    print('El arma de la compu es', arma_compu)
    



    #Indicar que el programa ha terminado
    #Validar si el usuario perdio
    if arma_compu =="papel" and mi_arma == "piedra" :
        print("perdiste")
    elif arma_compu =="tijera" and mi_arma == "papel":
        print("perdiste")
    elif arma_compu =="piedra" and mi_arma == "tijera":
        print("perdiste")



    #Validar quién gano


    if mi_arma == "piedra" and arma_compu == "tijera":
        print("ganaste")
    elif mi_arma == "papel" and arma_compu == "piedra":
        print("ganaste")
    elif mi_arma == "tijera" and arma_compu == "papel":
        print("ganaste")

    #Indicar si hubo empate
    elif mi_arma == arma_compu:
        print("Hubo un empate")


    print("FIN DEL PROGRAMA ")



    
