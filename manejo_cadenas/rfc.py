
if __name__ == '__main__':

    nombre = input('Escribe el nombre completo: ')
    fecha =  input('Escribe la fecha dd/mm/aaaa: ')
    
    #        Carlos Reséndiz Santillán
    primer_blanco = nombre.find(' ')
    nombre_usuario = nombre[0:primer_blanco]
    print(nombre_usuario)
    
    
