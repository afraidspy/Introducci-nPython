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

    def __str__(self) -> str:
        """
        Devuelve una cadena que representa al objeto estudiante.

        Returns:
        --------
        str
            La cadena que representa al objeto estudiante.
        """
        return f"Estudiante: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}"

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
        return self.__nombre == other.get_nombre() and self.__direccion == other.get_direccion() and self.__telefono == other.get_telefono()
