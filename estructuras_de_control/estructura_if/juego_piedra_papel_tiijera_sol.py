import random

if __name__ == '__main__':

    aleatorio =  random.randrange(1,4)
    mi_opcion = 0
    mi_arma = ''
    arma_compu = ''

    print("Escribe 1 para elegir piedra, 2 para elegir papel y 3 para elegir tijera: ")
    mi_opcion = int(input())

    if mi_opcion == 1:
        mi_arma = 'piedra'
    elif mi_opcion == 2:
        mi_arma = 'papel'
    elif mi_opcion == 3:
        mi_arma = 'tijera'
    else:
        print('El número escrito no es válido')

    if aleatorio == 1:
        arma_compu = 'piedra'
    elif aleatorio == 2:
        arma_compu = 'papel'
    elif aleatorio == 3:
        arma_compu = 'tijera'

    print('El arma del usuario es', mi_arma)
    print('El arma de la compu es', arma_compu)
