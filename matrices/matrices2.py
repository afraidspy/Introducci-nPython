class Matriz:
    def __init__(self, filas, columnas):
        self.__filas = filas
        self.__columnas = columnas
        self.__matriz = []

        self.__llenar()


    def __llenar(self):
        for i in range(self.__filas):
            fila = []
            for j in range (self.__columnas):
                 fila.append(0.0)
            self.__matriz.append(fila)
    
    def get_identidad(self):
        # Creamos una matriz de ceros del mismo tamaño que la matriz original
        identidad = Matriz(self.__filas, self.__columnas)

        # Recorremos la diagonal principal y asignamos 1 en cada posición
        for i in range(self.__filas):
            for j in range(self.__columnas):
                if i == j:
                    identidad.__matriz[i][j] = 1.0
        
        return identidad

    def llenar_valores_usuario(self):
        for i in range(self.__filas):
            for j in range(self.__columnas):
                self.__matriz[i][j] = float(input(f"Ingrese el valor para la posición [{i}][{j}]: "))

    def sumar_matrices(self, otra_matriz):
        if self.__filas != otra_matriz.__filas or self.__columnas != otra_matriz.__columnas:
            print("Las matrices deben tener las mismas dimensiones para poder sumarlas.")
        resultado = Matriz(self.__filas, self.__columnas)
        for i in range(self.__filas):
            for j in range(self.__columnas):
                resultado.__matriz[i][j] = self.__matriz[i][j] + otra_matriz.__matriz[i][j]
        return resultado
   
    def obtener_transpuesta(self):
        transpuesta = Matriz(self.__columnas, self.__filas)
        for i in range(self.__columnas):
            for j in range(self.__filas):
                transpuesta.__matriz[i][j] = self.__matriz[j][i]
        return transpuesta

    def es_simetrica(self):
        if self.__filas != self.__columnas:
            return False
        for i in range(self.__filas):
            for j in range(self.__columnas):
                if self.__matriz[i][j] != self.__matriz[j][i]:
                    return False
        return True
   
    def multiplicar(self, matriz_b):
        if self.__columnas != matriz_b.__filas:
            print("No se pueden multiplicar las matrices. El número de columnas de A no es igual al número de filas de B.")
            return None

        matriz_c = Matriz(self.__filas, matriz_b.__columnas)

        for i in range(self.__filas):
            for j in range(matriz_b.__columnas):
                suma = 0
                for k in range(self.__columnas):
                    producto = (self.__matriz[i][k] * matriz_b.__matriz[k][j])
                    suma += producto
                    print(f"i={i}, j={j}, k={k}, producto={producto} suma={suma}")
                matriz_c.__matriz[i][j] = suma

        return matriz_c

    def __str__(self):
        matriz_str = ""
        for i in range(self.__filas):
            for j in range(self.__columnas):
                matriz_str += str(self.__matriz[i][j]) + " "
            matriz_str += "\n"
           
        return matriz_str


matriz = Matriz(2,2)
matriz.llenar_valores_usuario()
print(matriz)
matriz2 = Matriz(2,2)
matriz2.llenar_valores_usuario()
print(matriz2)


print(matriz2.multiplicar(matriz2))

