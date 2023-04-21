from ejemplos_basicos import EjemplosListas

if __name__ == '__main__':

    lista = [[100.2,2,3],
             [1,3,4,3],
             [2,7,9,24.3]
            ]
    ejemplo =  EjemplosListas(lista)

    ejemplo.imprimir_matriz()

    ejemplo.sumar_elementos()

    print("Mayor",ejemplo.obtener_valor_maximo())
    print("Mayor mejorado: ",ejemplo.obtener_valor_maximo_mejor())

    print(ejemplo.filtrar_elementos(2))

    
