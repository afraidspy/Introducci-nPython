"""
Objetivo: Conocer cuál es la sintáxis
para implementar Herencia en Python
así como conocer la diferencia entre
una variable de clase y de instancia
@author: Jessica
"""

class Telefono(object):
    #Variable de clase
    contador = 0
    def __init__(self,numero):
        #Self.numero es una variable de instancia
        self.numero = numero
        #Variabl de clase
        Telefono.contador +=1

    def llamar(self, numero_salida):
        mensaje = 'Llamando  a {} desde el número {}'.format(numero_salida,self.numero)
        return mensaje

class TelefonoFijo(Telefono):
    contador_tel_fijo = 0
    def __init__(self, numero):
        super().__init__(numero)
        TelefonoFijo.contador_tel_fijo+=1
        self.ubicacion = "México"

    def activar_contestadora(self):
        print("Activando contestador")
        
class TelefonoCelular(Telefono):
    contador_celulares = 0
    def __init__(self, numero):
        super().__init__(numero)
        TelefonoCelular.contador_celulares+=1
        self.tipo = "iPhone"
    

"""telefono = Telefono("2323")
print(Telefono.contador)
print(telefono.llamar("99999999"))
"""

telefono_fijo = TelefonoFijo("11111111")#1
telefono_fijo2 = TelefonoFijo("222222")#2

print("Número de teléfonos fijos: ",TelefonoFijo.contador_tel_fijo)

num = input("Escribe número de telefono")
mi_iphone=TelefonoCelular(num)#3
num_otro= input("Escribe número de telefono al que vas a llamar")
print(mi_iphone.llamar(num_otro))

print("Número de teléfonos en total: ",Telefono.contador)#

"""telefono_fijo.llamar("33333")
print("Número de teléfonos fijos: ",TelefonoFijo.contador_tel_fijo)
print("Número de teléfonos en total: ",Telefono.contador)
"""




