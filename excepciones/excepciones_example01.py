"""
Script con ejemplo para manejar excepciones
Objetivo: Que el alumno conozca como se pueden manejar
diferentes tipos de excepciones y reconocer en qué momento se ejecuta cada una.
Recuerda que el bloque y else es opocional
"""

def pedir_edad():
        try:
            edad = int(input("Dame edad: "))
            edad +=5
            print("Edad estudiante: " + edad)
        except TypeError:
            print("Excepcion type por que no se puede concantenar Edad estudiante más edad")
        except ValueError:
            print("Se origina cuando se proporciona un número de otro tipo a int, o cuando se pasa una cadena")
        except Exception:
            print("Ocurrió una excpcion ")
        else:
            print("No ocurrió ninguna excepcion")
        finally:
            print("Siempre es un bloque que se ejecuta")

if __name__ == "__main__":
        pedir_edad()
    



    
