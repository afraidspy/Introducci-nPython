"""
    Objetivo: Que el alumno comprenda por qué y cómo se pueden crear excepciones personalzadas,
    que comprena como una excepción puede ser propagada y posteriormente como se maneja.
"""
#[1900,2005]
class AnioException(Exception):
    """Clase de excepción para manejar el año de nacimiento inválido."""

    def __init__(self, msg):
        super().__init__(msg)


class Student:
    """Clase que representa a un estudiante."""

    def __init__(self, nombre):
        """
        Inicializa una instancia de Student.

        Parametris:
            nombre (str): El nombre del estudiante.
        """
        self.nombre = nombre
        self.nac = 1900

    def set_anio_nac(self, anio):
        """
        Establece el año de nacimiento del estudiante.

        Parametros:
            anio (int): El año de nacimiento.

        Raises:
            AnioException: Si el año de nacimiento está fuera del rango de 1900 a 2005.
        """
        if anio < 1900 or anio > 2005:
            raise AnioException("Año fuera de rango")
        else:
            self.nac = anio


if __name__ == "__main__":

    student = Student("JS")

    try:
        student.set_anio_nac(1850)
    except AnioException as ae:
        print(ae)
        

        
