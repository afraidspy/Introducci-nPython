
from estudiante2 import Estudiante
from materia import Materia

if __name__ == "__main__":

    
    estudiante1 = Estudiante("Lola","Mexico","2342336423")
    estudiante2 = Estudiante("Rosa","Mexico","234236457433")
    estudiante3 = Estudiante("Diego","Mexico","453442342433")
    estudiante4 = Estudiante("Manuel","Mexico","56342342433")
    estudiante5 = Estudiante("José","Mexico","643342433")
    
    lista_materias = [Materia(1,"Programación", 10),
                      Materia(2,"Calculo", 7),
                      Materia(3,"Contabilidad", 6),
                      Materia(4,"Geometría Analítica", 9)]

    estudiante1.set_calificaciones(lista_materias)
    

    print(estudiante1)
