class Matriz:
    
    def __init__(self, filas:int, columnas:int):
        self.__filas = filas
        self.__columnas = columnas
        self.__matriz = []
        self.__llenar()


    def __llenar(self):
        for i in range(self.__filas):
            sublista = []
            for j in range(self.__columnas):
                sublista.append(0.0)
            self.__matriz.append(sublista)
     

   
    def llenar_valores_usuario(self):
        for i in range(self.__filas):
            for j in range(self.__columnas):
                valor = input("Escribe el valor de la casilla "+str(i) + "," + str(j))
                self.__matriz[i][j] = valor
                #print(self.__matriz[i][j], end = "")
            #print()
            
       
    def sumar_matrices(self, otra_matriz):
       pass
    def obtener_transpuesta(self):
        pass

    def es_simetrica(self):
      pass
    
    def multiplicar(self, matriz_b):
        pass


    def __str__(self):
        info = ""
        for i in range(self.__filas):
            for j in range(self.__columnas):
                info += str(self.__matriz[i][j]) + " "
            info += "\n"

        return info
            


matriz = Matriz(3,3)

matriz.llenar_valores_usuario()

