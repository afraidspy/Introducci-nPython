'''
    Programa que ilustra el uso de la instrucció continue
    dentro de un ciclo
    Autor: Jessica
'''
if __name__== "__main__":
    num = float(input('"Escribe un número:" '))
    while num > 0:
        num = num -1
        if num == 5:
            continue
        print ("Imprimiendo el valor de var: ", num)

