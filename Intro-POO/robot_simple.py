"""
    Ejemplo de una clase, la cuál contiene sus atributos públicos
    Autor: Jessica
"""
class Robot:
    def __init__(self):
        self.nombre = "Beto"
        self.peso = 200.0
        self.km = 1



if __name__ == '__main__':

    good_bunny = Robot()

    print(good_bunny.nombre)
    print(good_bunny.peso)
    print(good_bunny.km)

    robotina =  Robot()

    robotina.nombre = "Lola"
    robotina.km = 2
    robotina.peso = 50

    print(robotina.nombre)

    


    
        
