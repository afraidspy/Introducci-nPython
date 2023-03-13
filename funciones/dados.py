
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
import random

def tirar_dados()-> int:
    """
    Simula el lanzamiento de dos dados y devuelve la suma de los valores obtenidos.
    
    Returns:
        int: La suma de los valores obtenidos en los dos dados.
    """
    aleatorio1 = random.randrange(1, 7)
    print(f"Primer dado: {aleatorio1}")
    aleatorio2 = random.randrange(1, 7)
    print(f"Segundo dado: {aleatorio2}")
    return aleatorio1 + aleatorio2

def validar_suma()-> tuple[str, int]:
    """
    Simula el lanzamiento de dos dados y valida la suma de sus valores.
    
    Returns:
        tuple[str, int]: Una tupla que contiene el resultado del juego: "Ganaste", "Perdiste", o "Seguir Jugando":
                         y la suma de los valores obtenidos en los dos dados.
    """
    
    print("Se van a tirar 2 dados...")
    suma_dados = tirar_dados()
    print(f"La suma de los dados es: {suma_dados}")
    
    if suma_dados == 7 or suma_dados == 11:
        resultado = "Ganaste"
    elif suma_dados == 2 or suma_dados == 3 or suma_dados==12:
        resultado = "Perdiste"
    else:
        resultado = "Seguir Jugando"
    
    return resultado, suma_dados



def preguntar_repetir_juego()->bool:
    """
    Pregunta al usuario si desea volver a jugar, el usuario debe de escribir si ó no 
    
    Returns:
        bool: Regresa True si la respuesta del usuario es "SI", False en caso contrario.
    """
    resp = input("¿Quieres volver a jugar?[si/no]: ")
    return resp.upper().strip() == "SI"

def generar_reporte(total_juegos:int, total_ganados:int, total_perdidos:int):
    """
    Genera un reporte con el total de juegos jugados, el total de juegos ganados y el total de juegos perdidos.
    
    Params:
        total_juegos (int): El total de juegos jugados.
        total_ganados (int): El total de juegos ganados.
        total_perdidos (int): El total de juegos perdidos.
    
    Returns:
        None: La función no devuelve nada, simplemente imprime el reporte en la consola.
    """
    print("\nReporte:")
    print(f"Total de juegos jugados: {total_juegos}")
    print(f"Total de juegos ganados: {total_ganados}")
    print(f"Total de juegos perdidos: {total_perdidos}")

def jugar_dados():
    """
    Implementa el juego de dados y lleva un registro del total de juegos jugados, el total de juegos ganados
    y el total de juegos perdidos.

    Returns:
        None: La función no devuelve nada, simplemente imprime el resultado del juego y el reporte al final.
    """
    total_juegos = 0
    total_ganados = 0
    total_perdidos = 0
    seguir_jugando = True
    
    while seguir_jugando:
        total_juegos += 1
        resultado, suma_dados = validar_suma()
        print(resultado ,",", suma_dados)


        if resultado == "Seguir Jugando" :
            suma_pts_usuario = suma_dados
            suma_dados = tirar_dados()
            
        if (suma_dados == 7 or suma_dados==11 or suma_dados == suma_pts_usuario):
            print("Después de tirar de nuevo ganaste!!")
            total_ganados += 1
        else:
            print("Después de tirar de nuevo PERDISTE!!!!")
            total_perdidos +=1
            
        
        seguir_jugando = preguntar_repetir_juego()
        if not seguir_jugando:
            print("Fin del juego...")
            generar_reporte(total_juegos, total_ganados, total_perdidos)



if __name__ == '__main__':

     jugar_dados()
