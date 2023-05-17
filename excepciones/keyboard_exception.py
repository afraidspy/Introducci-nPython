try:
    while True:
        user_input = input("Ingrese un número: ")
        result = int(user_input) * 2
        print("El resultado es:", result)
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario")
