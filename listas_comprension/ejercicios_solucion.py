'''
Ejercicios

Objetivo: El alumno practicará la sintáxis  de listas por comprensión

Instrucciones: Resuelve los siguientes ejercicios, puedes entregar un archivo ed Python ó compartir el link de un notebook de Google Colab
ó entregar tus respuestas en una hoja antes de que termine la clase
'''

#1.Dada una lista llamada numeros, cuál sería la instrucción para que se generé la siguiente lista [(2, 4), (4, 8), (8, 16), (10, 20)]

numeros = [2,4,8,10]
resultado = [(x, x*2) for x in numeros if x % 2 == 0]

print("Resultado")
print(resultado)

#2. Dada una cadena, cuenta cuantos espacios tiene la cadena usando una lista por comprensión
cadena = "Usar listas por comprensión es más eficiente "
espacios = [caracter for caracter in cadena if caracter == ' ' ]
print("Espacios")
print(espacios)
print('Total: ',len(espacios))


#3. De la cadena anterior, elimina todas las vocales 
#Hint: Utiliza la función join() 

sin_vocales = "".join([caracter for caracter in cadena if caracter not in ["a","e","i","o","u"]])
print("Sin vocales")
print(sin_vocales)

#4. Indica que lista genera la siguiente instrucción. Explica tu resultado

lista = [(x, y, z) for x in range(1, 5) for y in 'ab' for z in range(2, 11, 2) if x%2 == 0 if (x*z) >= 1]

print(lista)

#5. Indica que imprime la lista genera el siguiente código, posteriormente crea el código equivalente haciendo uso de un for tradicional
resultados = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 11)]
print("Resultado usando listas por comprension")
print(resultados)
resultados = []
for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        resultados.append("FizzBuzz")
    elif i % 3 == 0:
        resultados.append("Fizz")
    elif i % 5 == 0:
        resultados.append("Buzz")
    else:
        resultados.append(i)
print("Resultado usando un for tradicional")
print(resultados)


