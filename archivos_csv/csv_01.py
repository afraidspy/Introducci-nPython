#https://docs.python.org/3/library/datetime.html
from datetime import datetime
date_now =  datetime.today().strftime('%Y-%m-%d')
##print(date_now)
"""
r: Abre el fichero en modo lectura.
r+: Si quieres leer y escribir en el fichero.
w: Para sobreescribir el contenido.
a: Para añadir al final del fichero en el caso de que ya exista.
"""
try:
    with open("estudiantes_info.csv",'w',encoding = 'utf-8') as file:
        file.write("Pedro,Medina,López,23"+","+date_now+"\n")
        file.write("Roberto,Luna,Solis,23"+","+date_now+"\n")
        file.write("Diana,González,Suárez,23"+","+date_now+"\n")
except FileNotFoundError:
    print("Archivo no encontrado")

try:
    with open("estudiantes_info.csv",'r',encoding = 'utf-8') as file:
        for line in file:
            data = line.split(',')
            #['Pedro', 'Medina', 'López', '23', '2022-06-01\n']
            print(data)
            nombre= data[0] + " " + data[1] + " " + data[2]
            edad = data[3]
            fecha = data[4]
            date_obj =  datetime.fromisoformat(fecha.replace("\n",""))
            print("Fecha: ", type(fecha))
            print("Fecha: ", type(date_obj))
        
except FileNotFoundError:
    print("Archivo no encontrado")

    
    

