
'''
Jugando dados 
Las reglas son:
Se tiran dos dados y se suma el valor de la cara superior de cada uno.
Si la suma es 7 u 11 el jugador gana.Si la suma es 2,3 0 12
el jugador pierde.
Si la suma es 4,5,6,8,9 ó 10, esta se convierte en los
puntos
del jugador, quien para ganar deberá volver a tirar los
dados; 
si en esta tirada la suma de puntos es 7 u 11, o es igual a la 
suma de la tirada anterior gana, en otro caso pierde.
En caso de perder o ganar,
tu programa deberá preguntarle al usuario
si desea volver a jugar dados.Al finalizar el programa deberás
de mostrarle al
usuario un reporte con la siguiente información:

Mostrar la cantidad de veces que el usuario ha jugado 
Mostrar la cantidad de veces que el usuario ha perdido
Mostrar la cantidad de veces que el usuario ha jugado
en total
'''

'''
Bienvenido, vamos a jugar  datos
Escribe tu nombre: Elsa Pato
Elsa Pato tira los dados
El primer dado tuvo 5 puntos y el segundo tuvo 4
Elsa Pato la suma es 9 por lo tanto vuelve a tirar
Elsa Pato la nueva suma es 12
¡PERDISTE!
'''

import random


seguir_jugando = True
total_juegos = 0
total_perdidos = 0
total_ganados = 0


nombre = input("Escribe tu nombre: ")
print(nombre,"Bienvenido vamos a jugar dados")

while (seguir_jugando):
    total_juegos+=1
    print("Tirando dados ...")
    aleatorio1 = random.randint(1,6) 
    aleatorio2 = random.randint(1,6)
    suma_dados = aleatorio1 + aleatorio2
    print("Primer dado: ", aleatorio1)
    print("Segundo dado:", aleatorio2)
    print("La suma de los dados es: ", suma_dados )
    if suma_dados == 7 or suma_dados == 11:
        print("Ganaste!!!")
        total_ganados+=1
    #2,3 0 12
    elif suma_dados == 2 or suma_dados == 3 or suma_dados==12:
        print("PERDISTE!!!!")
        total_perdidos+=1
        
    else: 
        suma_pts_user = suma_dados
        aleatorio1 = random.randint(1,6) 
        aleatorio2 = random.randint(1,6)
        suma_dados = aleatorio1 + aleatorio2
        if (suma_dados == 7 or suma_dados==11 or suma_dados==suma_pts_user):
            print("Después de tirar de nuevo ganaste!!")
            total_ganados+=1
        else:
            print("Después de tirar de nuevo PERDISTE!!!!")
            total_perdidos+=1
            
    resp = input("¿Quieres volver a jugar, escribe si/no")
    if (resp.upper()=="SI"):
        seguir_jugando = True
    else:
        seguir_jugando = False
   
print(nombre, " aquí puedes ver tu reporte: ")
print("Total de juegos jugados ", total_juegos)
print("Total de juegos jugados ganados ", total_ganados)
print("Total de juegos jugados  perdidos", total_perdidos)

