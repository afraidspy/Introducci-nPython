# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:14:29 2021

@author: sergi
"""

#EL PROPOSITO DE ESTA CLASE ES QUE DADA UNA POLIZA SE PUEDA CALCULAR LA CANTIDAD QUE LA ASEGURADORA
# LE PAGARÁ A UN ASEGURADO EN CASO QUE SE REPORTE UN SINIESTRO-Cabe mencionar que la cantidad que se
# pagará dependerá del deducible, del limite de la poliza y obviamente de la cantidad del siniestro
#Por otra parte tambien cabe mencionar que la cantidad del siniestro no necesariamente es igual
# a la cantidad que la aseguradora pagará 


# CASO 1) El monto del siniestro es menor que el deducible pago=0
# CASO 2) El monto del siniestro es mayor que el deducible pero menor que el limite pago=siniestro-deducible
# CASO 3) El monto del siniestro es mayor al limite entonces pago=limite
 
class Poliza: ## nombre de la clase 
    def __init__(self): ### constructor por omision  (public Poliza (){})
        

        self.vigencia = 2
        self.limite = 10000
        self.deducible = 2000
        self.siniestro = 0
        self.anioEmision=2021
        self.anioReclamo=0
        
    ### metodos getEl metodo get nos permite consultar el valor que nosotros asignamos a algun 
    ###atributo de algun objeto de   la clase se recomienda que haya un metodo get por cada atributo
    ### Los metodos gets no reciben parámetros a la hora de ser llamados
    ### Dentro del cuerpo del metodo se usa la palabra reservada return, seguida del nombre del atributo que devuelve
    
    def get_vigencia(self): #getVigencia
        return self.vigencia
    def get_limite(self):
        return self.limite
    def get_deducible(self):
        return self.deducible
    def get_siniestro(self):
        return self.siniestro
    def get_anioEmision(self):
        return self.anioEmision
    def get_anioReclamo(self):
        return self.anioReclamo
    
    
    
   ### Los metodos sets sirven para modificar el valor que le asignamos a algun parametro.
   #### Los metodos sets no devuelven resultados (vacios)  pues solo modifica los atributos.
   #al ser un metodo modificador, este tiene un dato de entrada que permitirá cambiar el viejo valor asignado por uno nuevo
   # A diferencia de los metodos Get,estos no utilizan dentro de su cuerpo la palabra reservada "return" 
   
    
    def set_vigencia(self,vig):
        self.vigencia=vig
    def set_limite(self,lim):
        self.limite=lim
    def set_deducible(self,dedu): # cantidad monetaria que comparte el asegurado con la aseguradora
        self.deducible=dedu
    def set_siniestro(self,sin):
        self.siniestro=sin
    def set_anioEmision(self,emi):
        self.anioEmision=emi
    def set_anioReclamo(self,rec):
        self.anioReclamo=rec
        
        
     #### metodo para saber si una poliza es vigente
     
    def es_vigente(self):
        return ((self.get_anioReclamo() - self.get_anioEmision()) <= self.get_vigencia())
    
    ### tipos de pago de la poliza
    
    def pago_c1(self):
        
        return 0
    
    def pago_c2(self):
        return self.get_siniestro()-self.get_deducible()
     
    def pago_c3(self):
        return self.get_limite()
    
    ### el metodo to string representa un objeto como una cadena de texto
    
    def __str__(self):
        return ' tu poliza tiene vigencia {} limite {}  deducible {}  siniestro {} anio de Emision {} anio de Reclamo {}'.format(self.vigencia,self.limite,self.deducible,self.siniestro,self.anioEmision,self.anioReclamo)
    
 

        
#### PRUEBA DE LA CLASE 
miPoliza=Poliza()

print(type(miPoliza))
print(miPoliza.vigencia)
print(miPoliza.get_vigencia())
miPoliza.set_vigencia(5)
print(miPoliza.get_vigencia())

print(miPoliza.get_limite())
miPoliza.set_limite(15000)
print(miPoliza.get_limite())

print(miPoliza.get_anioReclamo())
miPoliza.set_anioReclamo(2027) ### vigente hasta 2026 porque modificamos la vigencia a 5 años

print(miPoliza.get_anioReclamo())

print(miPoliza.es_vigente())


print(miPoliza.get_siniestro())
miPoliza.set_siniestro(20000)
print(miPoliza.get_siniestro())


if (miPoliza.get_siniestro()>= miPoliza.get_deducible()) & (miPoliza.get_siniestro() <miPoliza.get_limite()):
    print("tu pago es de ",miPoliza.pago_c2())

if miPoliza.get_siniestro()<miPoliza.get_deducible():
    print("tu pago es de ",miPoliza.pago_c1())

if miPoliza.get_siniestro()>miPoliza.get_limite():
    print("tu pago es de ",miPoliza.pago_c3())
    
print(miPoliza.__str__())
#


