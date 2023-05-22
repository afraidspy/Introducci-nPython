#Abrir un archivo de texto solo para lectura
'''
A continuación, te muestro cómo abrir un archivo indicando
explícitamente el modo de acceso (solo lectura).
El estatuto for se encarga de recorrer línea por línea
el archivo e ir almacenando el contenido en la variable line
para poder imprimirlo.
Si el archivo que se manda como parámetro a la función
open no se encuentra, entonces Python nos
va a arrojar un error de entrada / salida (I/O) al momento de ejecutar nuestro script.
'''

"""
abrir
procesar: leer o escribir
cerrar
"""
try:
  file_handler = open('./ejemplo.txt', 'r')
#Si el archivo no contiene texto, es decir está vació, entonces
#no se imprime nada en consola
  for line in file_handler:
    print(line)
  file_handler.close()
except FileNotFoundError:
    print("Archivo no encontrado")
