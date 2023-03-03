#Escribir un programa que pida al usuario un número positivo. 
#El programa deberá terminar hasta que el usuario
#escriba la palabra fin. Al finalizar el programa deberá de mostrar el
#número más pequeño y el número más grande
#que el usuario haya introducido

# 2, 10,15,0,20


##TERMINAR EL SIGUIENTE PROGRAMA

peque = None
grande = None

while True:
    num = input("Escribe un número positivo o fin/FIN si deseas terminar el programa")
    if (num.upper().strip() == "FIN"):
        break
    else:
        num_int = int(num)#2
        if (num_int < 0):
            print("Por favor, solo acepto números positivos...")
        else:
            if(peque == None):  
                peque = num_int
            if (grande == None):
                grande = num_int
                
            if (num_int > grande):
                grande = num_int
            if num_int < peque:
                peque = num_int

print("El elemento más pequeño es:", peque)
print("El elemento más grande es: ", grande)
