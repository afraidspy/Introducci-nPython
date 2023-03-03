'''
    Programa que hace uso del while y convierte
    un número decimal a un número binario
    Autor: Jessica
'''
if __name__ == "__main__":
    decimal = int(input("Ingrese un número: "))
    cociente = decimal
    binario = ""
    while cociente > 0:
        residuo = str(cociente % 2)
        cociente //= 2
        binario = residuo + binario

    print("El número en binario es: ", binario)

##Ejercicio: Escribe ahora el código para convertir una cadena, 
# el cuál representa un número binario a decimal
    
    
