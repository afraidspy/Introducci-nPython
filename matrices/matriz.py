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
                valor = float( input("Escribe el valor de la casilla "+str(i) + "," + str(j)))
                self.__matriz[i][j] = valor
                #print(self.__matriz[i][j], end = "")
            #print()
            
       
    def sumar_matrices(self, otra_matriz):

        ##suma_m = Matriz(self.__filas, self.__columnas)
        if self.__filas == otra_matriz.__filas and self.__columnas == otra_matriz.__columnas:
            suma_m = Matriz(otra_matriz.__filas, otra_matriz.__columnas)

            for i in range(self.__filas):
                for j in range(self.__columnas):                    
                    suma_m.__matriz[i][j] = self.__matriz[i][j] + otra_matriz.__matriz[i][j]

            return suma_m                
        else:
            print("Las matrices deben de ser de las mismas dimensiones")

            return None
        
      
    
    def obtener_transpuesta(self):
        transpuesta_matriz = Matriz(self.__columnas, self.__filas)

        for i in range(transpuesta_matriz.__filas):
            for j in range(transpuesta_matriz.__columnas):

                transpuesta_matriz.__matriz [i][j] = self.__matriz [j][i]

        return transpuesta_matriz

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
            


