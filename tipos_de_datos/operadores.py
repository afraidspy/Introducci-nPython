'''
    Ejemplos para manejar diferentes operadores
    en Python
    Autor: Jessica
'''

#Aquí empieza la ejecución principal de un programa
if __name__ == "__main__":
    #Operadores aritméticos
    resultado =  46 % 9
    print(f'Resultado {resultado}')
    resultado =  46 % 9 + 4 * 4 - 2
    print(f'Resultado {resultado}')
    resultado *=2 * 3 + (23 * 3 % 2)
    print(f'Resultado {resultado}')

    #Operadores lógicos
    x = 5
    y = 7
    z = 8   
    resultado = x < y and (y < z or x == 5)
    print("Resultado = ", resultado)

    #Operadores Binarios
    a = 0b11110 
    b = 0b10011 
    print ("a = ", a)
    print ("b = " ,b)
    print("a|b = ", a | b)
    print("a&b = ", a & b)
    print("a<<2 = ", a << 2)
    print("a>>2 = ", a >> 2)
    '''
        Se comparan los bits en cada posición
        dónde 1 == True y 0 == False'''
    print("a|b = ", a | b) #OR  - 10111 == 23
    print("a&b = ", a & b) #AND - 10000 == 16
    print("a^b = ", a ^ b) #XOR - or exclusivo == 00111 = 7
    '''
        Todos los bits de a se desplazan a la IZQUIERDA n posiciones,
        en este caso n=2, es decir: se agregan
        n=2 números a la derecha.
    '''
    print("a<<2 = ", a << 2) #0b10001=>0b10001 00
    '''
        Todos los bits de a se desplazan a la DERECHA n posiciones,
        en este caso n=2, se insertan n=2 ceros en los bits vacantes a la izquierda.
        n=2 números a la derecha.
    '''
    print("a>>2 = ", a >> 2) #0b10001=>0b00100

