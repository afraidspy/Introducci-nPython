# La herencia es la capacidad que tiee una clase de heredar los atributos y metodos de otra, algo que nos permite reutilizar codigo y hacer programas mas optimos
# Estos nos permite partir de una clase con muchos atributos y posteriormente descomponer en otras clases mas simples que nos permitan trabajar mejor con sus datos
# La herencia multiple es la capacidad de una subclase de heredar de multiples super clases
# El problema que conlleva esto es que si varias superclases tienen los mismos atributos o metodos, la subclase solo hereda una de ellas
# En este caso python dara prioridad a las clases mas a la izquierda en el momento de la declaracion



class Vehiculo:
    def __init__(self,color,anio,marca,motor):
        self._color=color
        self._anio=anio
        self._marca=marca
        self._motor=motor

    def arrancar(self):
        print("vehiculo en movimiento")
    def frenar(self):
        print("vehiculo sin movimiento")

miVehiculo = Vehiculo("rojo",2022,"Tesla","motor sencillo")

miVehiculo.arrancar()
miVehiculo.frenar()


print("clase motocicleta")
print("............")

class Motocicleta(Vehiculo):
    def __init__(self,ruedas,color,anio,marca,motor):
        self.__ruedas=ruedas
        Vehiculo.__init__(self,color,anio,marca,motor)#Pueden usar super

    def avanzar(self):
        print("vehiculo avanzando por tierra")

mimoto= Motocicleta(2,"verde",2020,"yamaha","motor pro")

mimoto.arrancar()
mimoto.avanzar()
mimoto.frenar()

print("clase helicoptero")
print("............")

class Helicoptero(Vehiculo):
    def __init__(self,helice,color,anio,marca,motor):
        self.__helice=helice
        Vehiculo.__init__(self,color,anio,marca,motor)

    def volar(self):
        print("vehiculo avanzando por aire")

mihelicoptero= Helicoptero("helice normal","verde",2020,"yamaha","motor pro")

mihelicoptero.arrancar()
mihelicoptero.volar()
mihelicoptero.frenar()

#Herencia múltiple es una caracteristica de Python
class MotoAerea(Helicoptero,Motocicleta):
    def __init__(self,ruedas,helice,color,anio,marca,motor):
        Helicoptero.__init__(self,helice,color,anio,marca,motor)
        Motocicleta.__init__(self,ruedas,color,anio,marca,motor)
mimotoaerea= MotoAerea(2,"helice normal","verde",2020,"yamaha","motor pro")
mimotoaerea.arrancar()
mimotoaerea.volar()
mimotoaerea.avanzar()
mimotoaerea.frenar()


vehicculos = [Motocicleta(4,"rojo",2023,"Ford","motor"), Helicoptero("helice normal","verde",2020,"yamaha","motor pro")]
print("Ejemplo de polimorfismo")
print("...............................")
for i in vehicculos:
    i.arrancar()
    if isinstance(i,Helicoptero):
        i.volar()
    



        




