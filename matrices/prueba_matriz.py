from matriz import Matriz

if __name__ == "__main__":

    while True:
        
        print("Calculadora de matrices")
        print("[0] SALIR")
        print("[1] Sumar matrices")
        print("[2] Restar matrices")
        print("[3] Multiplicar matrices")
        print("[4] Obtener transpuesta")
        opcion = int(input("Elige una opción: "))
        
        match opcion:
            case 0:
                print("Fin")
                break;
            case 1:
                print("Suma")
                m1 = Matriz(2,2)
                m1.llenar_valores_usuario()
                print(m1)   
                m2 = Matriz(2,2)
                m2.llenar_valores_usuario()
                print(m2)

                suma = m1.sumar_matrices(m2)
                print(suma)
                
            case 2:
                print("Identidad")
                m3 = Matriz(3,3)
                iden= m3.get_identidad()
                print(iden)
                
            case 3:
                print("Multiplicación")
            case 4:
                print("Transpuesta")
                m1 = Matriz(2,3)
                m1.llenar_valores_usuario()
                print(m1)
                transpuesta = m1.obtener_transpuesta()
                print(transpuesta)
            case 5:
                print("Identidad")
                m3 = Matriz(3,3)
                iden= m3.get_identidad()
                print(iden)
                
                
