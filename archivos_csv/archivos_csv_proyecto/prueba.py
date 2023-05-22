
"""

Script para probar el manejo de archivos
@author: guest
"""

from Pregunta import Pregunta
from Respuesta import Respuesta

from gestor_preguntas import ManejadorPreguntasAbstract
from gestor_preguntas import ManejadorPreguntas

from gestor_archivos import GestorArchivosAbstract
from gestor_archivos import ArchivoCSV


manejador_preguntas = ManejadorPreguntas(ArchivoCSV("preguntas.csv"))
preguntas = []

def mostrar_menu():
    print("----- MENU -----")
    print("[0]. Salir")
    print("[1]. Agregar pregunta")
    print("[2]. Mostrar todas las preguntas")
    print("[3]. Modificar pregunta")
    print("[4]. Borrar pregunta")
    print("-----------------")

def escribir_pregunta():
    tipo = input("Elige el tipo de pregunta que vas a agregar \n"+
                 " [1] Con una respuesta correcta"+
                 " [2] Con dos respuestas correctas: ")
    if tipo == "1":
        
       descripcion =  input("Escribe la descripción de la preungta: ")
       respuesta_valida = input("Escribe la respuesta que será válida: ")
       respuesta1 = Respuesta(respuesta_valida,True)
       respuesta_invalida1 = input("Escribe una respuesta NO válida: ")
       respuesta2 = Respuesta(respuesta_invalida1,False)
       respuesta_invalida2 = input("Escribe OTRA respuesta NO válida: ")
       respuesta3 = Respuesta(respuesta_invalida2,False)
       lista_respuestas = [respuesta1,respuesta2,respuesta3]
       pregunta = Pregunta(1,descripcion)
       pregunta.agregar_respuesta(lista_respuestas)
       print("Se creó la pregunta de tipo1:")
       print(pregunta)
       
       manejador_preguntas.agregar_pregunta(pregunta)
       
       
    elif tipo == "2":
        descripcion =  input("Escribe la descripción de la preungta: ")
        respuesta_valida1 = input("Escribe la primer respuesta que será válida: ")
        respuesta1 = Respuesta(respuesta_valida1,True)
        respuesta_valida2 = input("Escribe la segunda respuesta que será válida: ")
        respuesta2 = Respuesta(respuesta_valida2,True)
        
        respuesta_invalida1 = input("Escribe una respuesta NO válida: ")
        respuesta3 = Respuesta(respuesta_invalida1,False)
        respuesta_invalida2 = input("Escribe OTRA respuesta NO válida: ")
        respuesta4 = Respuesta(respuesta_invalida2,False)
        lista_respuestas = [respuesta1,respuesta2,respuesta3,respuesta4]
        pregunta = Pregunta(2,descripcion)
        pregunta.agregar_respuesta(lista_respuestas)
        
        print("Se creó la pregunta de tipo 02:")
        print(pregunta)
        
        
        manejador_preguntas.agregar_pregunta(pregunta)

    else:
       print("Opción inválida. Por favor, seleccione una opción válida.")


def leer_preguntas():
    preguntas = manejador_preguntas.leer_todas_pregunta()
    
    print(preguntas)

def modificar_pregunta():
    # Lógica para modificar una pregunta
    pass

def borrar_pregunta():
    # Lógica para borrar una pregunta
    pass





while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
            
    if opcion == "1":
       escribir_pregunta()
    elif opcion == "2":
        leer_preguntas()
    elif opcion == "3":
        modificar_pregunta()
    elif opcion == "4":
        borrar_pregunta()
    elif opcion == "0":
        print("Saliendo del programa y guardando cambios...")
        
        manejador_preguntas.guardar_preguntas()
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


