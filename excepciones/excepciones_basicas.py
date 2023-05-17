"""
Ejemplo para poder terminar el programa de forma abrupta

"""
import sys


def ejemplo_excepcion():
    try:
        print("Antes de llamar a sys.exit()")
        sys.exit(0)
        print("Después de llamar a sys.exit()")
    except SystemExit:
        print("Entrando al excepto para manejar la excepcion SystemExit")
    finally:
        print("Finalizando el programa")

if __name__ == "__main__":
    ejemplo_excepcion()

