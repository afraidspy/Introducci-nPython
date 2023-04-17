"""
    Clase con ejercicios relacionados a listas de listas
    Objetivo: Que el alumno pueda analizar como iterar
    en listas de listas

    lista_numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    lista_texto = [['hola', 'mundo'], ['esta', 'es', 'una', 'frase'], ['otra', 'frase', 'para', 'ejemplo']]
    
    lista_booleanos = [[True, False], [False, True, True], [False, False, True]]
    
    lista_mixta = [[1, 'a', True], ['b', False], [2, 'c', True, False]]


"""

class EjemplosListas:

    def __init__(self, lista:list):
        self.__lista = lista

    def sumar_elementos(self)->float:
        """
            Método que devuelve la suma de todos sus elementos
        """
        sum = 0
        for i in self.__lista:
            sublista = i
            for j in sublista:
                sum += j

        return sum
                
    def obtener_valor_maximo(self)->float:
        """
            Método que devuelve la suma de todos sus elementos
        """
        maximos = []
        for i in self.__lista:
            sublista = i
            maximo = max(sublista)
            maximos.append(maximo)
        return max(maximos)

    def obtener_valor_maximo_mejor(self)-> float:
        max= self.__lista[0][0]
        for i in self.__lista:
            sublista = i
            for j in sublista:
                if j>max:
                    max = j
        return max
            
    def filtrar_elementos(self, valor:float) ->list:
        """
            Método que devuelve una lista con los elementos que son mayores que un valor dado.
            Params:
                valor(float) -  El valor a considerar
        """
        pass

    def imprimir_matriz(self):
        for i in self.__lista:
            sublista = i
            for j in sublista:
                print (j, end = " ")
            print()




        
