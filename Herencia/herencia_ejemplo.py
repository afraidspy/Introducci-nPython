class EmpleadoPorComision:

    def __init__(self,nombre, apellido_paterno, num_seg_social,ventas,comision):
        ##atributo protegido ==> es heredado a la clase hija
        ## con dos guiones bajos ==> atributos privados
        self._nombre = nombre
        self._paterno = apellido_paterno
        self._num_seg_social = num_seg_social
        self._ventas = ventas
        self._comision = comision
    
    def calcular_ingreso(self):
        return self._ventas * self._comision
    
    
    def __str__(self):
        return self._nombre + "-" + self._paterno + "-"+self._num_seg_social+"-"+str(self._ventas)+"-"+str(self._comision)
"""
    Implementación de una clase hija
"""       
class EmpleadoBaseComision(EmpleadoPorComision):
    
    def __init__(self,nombre, apellido_paterno, num_seg_social,ventas,comision,sueldo_base):    
        super().__init__(nombre, apellido_paterno, num_seg_social,ventas,comision)
        
        self.__sueldo_base = sueldo_base
    
    def obtener_sueldo_base(self):    
        return self.__sueldo_base
    
    def calcular_ingreso(self):
        return super().calcular_ingreso() +  self.__sueldo_base
    
    def __str__(self):
        return super().__str__() + "- " + str(self.__sueldo_base)
    
        
    
    
"""
empleado = EmpleadoPorComision("Elsa","Pato","30505",200, 50)
print(empleado)
print("Sueldo: ", empleado.calcular_ingreso())


is_objeto = isinstance ( empleado, EmpleadoPorComision)
print(is_objeto)

empleado_base = EmpleadoBaseComision("Patricio","Pérez","12024",200,50,1000)
print(empleado_base)

print("ingreso ", empleado_base.calcular_ingreso())
"""
list_empleados = [ 
                    EmpleadoPorComision("E0","Ap0","30505",200,50),
                    EmpleadoBaseComision("E1","Ap1","30505",200,50,1000),
                    EmpleadoBaseComision("E2","Ap2","30505",100,50,1000),
                    EmpleadoBaseComision("E3","Ap3","30505", 20,50,1000),
                    EmpleadoPorComision("E4","Ap4","30505",100,50),
                  ]
#Poliformismo
for item in list_empleados:
    print(type(item))
    print("Ingreso: ", item.calcular_ingreso())



