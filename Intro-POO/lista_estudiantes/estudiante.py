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


    def set_calificaciones(lista):
        self.__calificaciones = lista


    def promedio():
        """
            Calcula el promedio de las calificaciones almacenadas en el atributo privado __calificaciones.
            Returns:
            float: El promedio de calificaciones
        """
        sum = 0
        for i in self.__calificaciones:
            sum += i

        return sum / len(self.__calificaciones)

    def agregar_calificacion(calif:float):
        """
            Agrega una calificación a la lista de calificaciones almacenadas en el atributo privado __calificaciones.

            Params:
            calificacion (float): La calificación a agregar a la lista.
    
        """
        self.__calificaciones.append(calif)


    def eliminar_calificacion(pos:int):
        """
           Elimina una calificación de la lista de calificaciones almacenadas en el atributo privado __calificaciones.

           Params:
           pos (int): La posición de la calificación que se va a eliminar en la lista.

        """
        if pos > 0 and pos < len(self.__calificaciones):
            self.__calificaciones.pop(pos)
        
    def obtener_calif_mas_alta()-> float:
        """
            Obtiene el valor de la calificación más alta
            Returns
            float: El valor con la calificación más alta
        """
        """
        max = self.__calificaciones[0]
        for i in range(0, len(self.__calificaciones))
            if self.__calificaciones[i] > max:
                max = self.__calificaciones[i]
        """

        return max(self.__calificaciones) 

    def obtener_calificaciones_mas_altas()-> float:
        """
            Obtiene los índices de todas las calificaciones más altas
            Returns:
            [int] : Regresa la lista con los índices de las calificaciones más altas
        """
        max = []
        for i in range(0, len(self.__calificaciones))
            if self.__calificaciones[i] == self.obtener_calif_mas_alta():
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
        return f"Estudiante: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}, Calificaciones : {self.__calificaciones}"

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
