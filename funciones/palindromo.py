'''
    Programa para validar si una cadena es un palíndromo
    Objetivo: Que el alumno pueda analizar diferentes soluciones
    a un mismo problema para elegir la más eficiente.
    Autor: Jessica
'''
'''
    Función que valida si una cadena es palíndromo, tomando en cuenta
    si la longitud de la cadena es par o impar
    cadena : la cadena a validar
    bool: Regresa True si es palindromo y False en otro caso
'''
def validar_palindromo(cadena:str)-> bool:
    tam = len(cadena)

    if tam % 2 == 0:
        i = 0
        j = tam - 1

        while j > i :
            if cadena[i] != cadena[j]:
                return False
            i+= 1
            j-= 1
    else:
         mitad = tam // 2
         i = 0
         j = tam - 1
        
         while i < mitad :
             if cadena[i] != cadena[j]:
                return False
             i += 1
             j -= 1
    

    return True
'''
    Función que valida si una cadena es palíndromo, NO se toma en
    cuenta la longitud  de la cadena, ya que el algoritmo funciona para ambos casos.
    cadena : la cadena a validar
    bool: Regresa True si es palindromo y False en otro caso
'''
def validar_palindromo_2(cadena: str) -> bool:
    tam = len(cadena)
    mitad = tam // 2
    i = 0
    j = tam - 1

    while i < mitad:
        if cadena[i] != cadena[j]:
            return False
        i += 1
        j -= 1

    return True

'''
    Función que valida si una cadena es palíndromo,usando un for
    y recorriendo los carácteres de atrás hacia adelante con
    la siguiente operación tam - i - 1
    cadena : la cadena a validar
    bool: Regresa True si es palindromo y False en otro caso
'''
def validar_palindromo_mejorada(cadena: str) -> bool:
    tam = len(cadena)
    for i in range(tam // 2):
        if cadena[i] != cadena[tam - i - 1]:
            return False
    return True

'''
    Función simplificada que valida si una cadena es palíndromo, haciendo uso de slice
    en las cadenas
    cadena : la cadena a validar
    bool: Regresa True si es palindromo y False en otro caso
'''
def validar_palindromo_slice(cadena:str) -> bool :

    return cadena == cadena[::-1]




if __name__ == "__main__":

    print(validar_palindromo('AABBAA'))
    print(validar_palindromo_2('AABBAA'))
    print(validar_palindromo_mejorada('AABBAA'))
    print(validar_palindromo_slice('AABBAA'))
