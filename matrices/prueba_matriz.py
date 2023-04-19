from matriz import Matriz

if __name__ == "__main__":

    while True:

        matriz =  Matriz(4,4)
        print(matriz)

        matriz.llenar_valores_usuario()

        print(matriz)
        
        print("Calculadora de matrices")
        print("[0] SALIR")
        print("[1] Sumar matrices")
        print("[2] Restar matrices")
        print("[3] Multiplicar matrices")
        
        opcion = int(input("Elige una opción: "))

       
        
        
        match opcion:
            case 0:
                print("Fin")
                break;
            case 1:
                print("Suma")
            case 2:
                print("Resta")
                
            case 3:
                print("")
                
