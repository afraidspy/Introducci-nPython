
def validar_palindromo(cadena:str)-> bool:
    tam = len(cadena)

    if tam % 2 == 0:
        i = 0
        j = tam - 1
        print(i,",", j)

        while j > i :
            if cadena[i] != cadena[j]:
                print("Entrando..");
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

def validar_palindromo_mejorada(cadena: str) -> bool:
    tam = len(cadena)
    for i in range(tam // 2):
        if cadena[i] != cadena[tam - i - 1]:
            return False
    return True





if __name__ == "__main__":

    print(validar_palindromo('AABBAA'))
    print(validar_palindromo_2('AABBAA'))
    print(validar_palindromo_mejorada('AABBAA'))
