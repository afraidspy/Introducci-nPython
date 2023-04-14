from materia import Materia

class Estudiante:
    """
    Clase para representar a un estudiante.

    Atributos:
    ----------
    __nombre : str
        El nombre del estudiante.
    __direccion : str
        La dirección del estudiante.
    __telefono : str
        El teléfono del estudiante.
    """

    def __init__(self, nombre: str, direccion: str, telefono: str):
        """
        Constructor de la clase Estudiante.

        Parámetros:
        -----------
        nombre : str
            El nombre del estudiante.
        direccion : str
            La dirección del estudiante.
        telefono : str
            El teléfono del estudiante.
        """
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__calificaciones = []

    def get_nombre(self) -> str:
        """
        Obtiene el nombre del estudiante.

        Retorna:
        --------
        str
            El nombre del estudiante.
        """
        return self.__nombre

    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre del estudiante.

        Parámetros:
        -----------
        nombre : str
            El nuevo nombre del estudiante.

        Returns:
        --------
        None
        """
        self.__nombre = nombre

    def get_direccion(self) -> str:
        """
        Obtiene la dirección del estudiante.

        Returns:
        --------
        str
            La dirección del estudiante.
        """
        return self.__direccion

    def set_direccion(self, direccion: str) -> None:
        """
        Establece la dirección del estudiante.

        Paráms:
        -----------
        direccion : str
            La nueva dirección del estudiante.

        Retursn:
        --------
        None
        """
        self.__direccion = direccion

    def get_telefono(self) -> str:
        """
            Obtiene el teléfono del estudiante.

            Returns:
            --------
            str
                El teléfono del estudiante.
        """
        return self.__telefono

    def set_telefono(self, telefono: str) -> None:
        """
            Establece el teléfono del estudiante.

            Paráms:
            -----------
            telefono : str
                El nuevo teléfono del estudiante.

            Retursn:
            --------
            None
        """
        self.__telefono = telefono


    def set_calificaciones(self, lista):
        self.__calificaciones = lista


    def promedio(self):
        """
            Calcula el promedio de las calificaciones almacenadas en el atributo privado __calificaciones.
            Returns:
            float: El promedio de calificaciones
        """
        sum = 0
        for materia in self.__calificaciones:
            sum += materia.get_calificacion()

        return sum / len(self.__calificaciones)

    def agregar_materia(self, materia:object):
        """
            Agrega una calificación a la lista de calificaciones almacenadas en el atributo privado __calificaciones.

            Params:
            calificacion (float): La calificación a agregar a la lista.
    
        """
        for i in self.__calificaciones:
            if i == materia:
                print("Ya existe la materia")
            else:
                self.__calificaciones.append(materia)


    def eliminar_materia(self,codigo:int):
        """
           Elimina una calificación de la lista de calificaciones almacenadas en el atributo privado __calificaciones.

           Params:
           pos (int): La posición de la calificación que se va a eliminar en la lista.

        """

        for i in self.__calificaciones:
            if  i.get_codigo() == codigo:
                self.__calificaciones.remove(i)
            else:
                print("No se encuentra el código")
        
        
    def obtener_calif_mas_alta(self)-> float:
        """
            Obtiene el valor de la calificación más alta
            Returns
            float: El valor con la calificación más alta
        """
        
        max = self.__calificaciones[0]
        for i in range(0, len(self.__calificaciones)):
            if self.__calificaciones[i].get_calificacion() > max.get_calificacion():
                max = self.__calificaciones[i]
    
        return max.get_calificacion()        

    def obtener_calificaciones_mas_altas(self)-> float:
        """
            Obtiene los índices de todas las calificaciones más altas
            Returns:
            [int] : Regresa la lista con los índices de las calificaciones más altas
        """
        max = []
        for i in range(0, len(self.__calificaciones)):
            if self.__calificaciones[i].get_calificacion() == self.obtener_calif_mas_alta():
                max.append(i)

        return max


    def __str__(self) -> str:
        """
        Devuelve una cadena que representa al objeto estudiante.

        Returns:
        --------
        str
            La cadena que representa al objeto estudiante.
        """
        info_materias = ""

        for materias in self.__calificaciones:
            info_materias += materias.__str__() + "\n"
            
        return f"Estudiante: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}, Calificaciones :\n {info_materias}"

    def __eq__(self, otro: 'Estudiante') -> bool:
        """
        Compara dos objetos estudiante y devuelve True si sus atributos son iguales.

        Params:
        -----------
        other : Estudiante
            El otro objeto estudiante a comparar.

        Returns:
        --------
        bool
            True si los objetos son iguales, False de lo contrario.
        """
        if not isinstance(otro, Estudiante):
            return False
        return self.__nombre == other.get_nombre() and self.__direccion == other.get_direccion() and self.__telefono == other.get_telefono() and self.__calificaciones == otro.get_calificaciones()
