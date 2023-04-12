    
def sumar_numeros():  #En otro lenguajes si no regresa nada la función , se usa la palabra reservada void
    num1 =  int(input('Nu


                    m1: '))
    num2 =  int(input('Num2: '))
    sumNums = str(num1 + num2)
    print('La suma es: ' + sumNums)


def imprimir_mensaje(nombre:str):
    print('Bienvenido al curso ' + nombre)


def imprimir_mensaje_curso(nombre:str,curso:str):
    print('Bienvenido al curso ' +curso+ " " + nombre)

def multiplicar_numeros()-> int:
    num1 =  int(input('-Num1: '))
    num2 =  int(input('-Num2: '))
    return num1 * num2

def calcular_perimetro_cuadrado(a:float)->float:
    #print("funciones_ejemplo.py")
    mult = 4*a
    print("Mult, ", mult)
    return mult

def obtener_menor(a=1,b=10):
    if (a<b):
        return a
    else:
        return b

if __name__ == "__main__":
    
    #sumar_numeros()
    #imprimir_mensaje('Chewbaka')
    imprimir_mensaje_curso('Pedro','Progra')
    #a = 4
    #tipo = type(a) #int
    #nombre = input("Dame nombre: ")
    #curso = input("Dame curso: ")
    #imprimir_mensaje_curso(nombre, curso)

##    result = multiplicar_numeros()
##    print('Resultado = ',result)
##
    lado = float(input('lado: '))
    perimetro = calcular_perimetro_cuadrado(lado)
    print("Perimetro", perimetro)

    #menor = obtener_menor()
    #print("El menor es ", menor)
    #menor = obtener_menor(7,20)
    #print("El menor es ", menor)
