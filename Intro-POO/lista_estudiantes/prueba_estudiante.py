from estudiante import Estudiante

if __name__ == "__main__":


    while True:
        print(" [0] Salir\n" + 
               "[1] Agregar calificacion\n" + 
               "[2] Obtener promedio\n" + 
               "[3] Obtener calif más alta\n")

        opcion = int(input("Escribe una opción: "))

        estudiante = Estudiante("Carlos","México","5588567456")

        match opcion:
            case 0:
                print("Fin del programa")
                break;
            case 1:
                calif = float(input("Dame la calif de progra: "))
                estudiante.agregar_calificacion(calif)
                #Agregar las demás calificaciones
                
            case 2:
                print("Promedio " ,  estudiante.promedio())
            case 3:
                print("Calif más grande " ,  estudiante.obtener_calif_mas_alta())
