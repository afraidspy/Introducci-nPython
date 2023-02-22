'''
    Programa para conocer la estructura de control if
    y sus variantes
    Autor: Jessica
    Objetivo if: Modificar el flujo de ejecución del programa
    y realizar programas más robustos.
'''
'''
    Sintáxis de un if
    codigoDePrograma
    if (condicion1==True):
     codigo1
    codigoDePrograma
'''

###### inicio if
if __name__ == '__main__':
    edad = 15
    print("**Ejecución de un if simple")
    print("¿Eres mayor de edad?")

    if edad >=18:
        print("Eres mayor de edad, ya puedes tramitar tu INE")
        
    print("Hasta luego! :) ")
    ###### final if
          
    ##### inicio if else
    edad=15
    print("hola")
    '''
    ### codigo_del programa
    ### if (condicion1==True):
    ###     codigo1
    ### else:
    ###     codigo2
    ### codigoDePrograma
    '''
    print("**Ejecución de un if else")
    if edad >= 18:
        print("Eres mayor de edad,ya puedes sacar tu INE")
    else:
        print("Eres menor de edad, aún no puedes sacar tu INE")

    print("Hasta luego")

    ####final if else

    '''
        inicio elif
    '''
    print("**Ejecución de elif")
    edad=15

    if edad >18:
        print("Eres mayor de edad")
    elif edad==18:
        print("Recientemente eres mayor de edad")
    else:
        print("menor de edad")
        
    print("hasta luego")
    ##### final elif



##### inicio condiciones anidads
    edad=20

    print("**Ejecución de if anidado")

    if edad>=18:
        if edad==18:
            print("Acabas de cumplir 18,bienvenido al club")
        else:
            print("Eres mayor de edad,bienvenido al club")
    else:
        print("Eres menor de edad, no puedes ser parte del club")

    print("Hasta luego")

##### final condiciones anidadas
