
if __name__ == '__main__':

    nombre = input('Escribe el nombre completo: ').strip()
    fecha =  input('Escribe la fecha dd/mm/aaaa: ').strip()
    
    # Carlos Reséndiz Santillán
    # 07/05/2004
    # 0123456789
    # RESCO040507
    indice_primer_espacio = nombre.find(' ')
    #print("Indice: " ,indice_primer_espacio)
    #Se obtiene solo el nombre
    nombre_usuario = nombre[0:indice_primer_espacio]
    #Obtener solo el apellido paterno
    subcad = nombre[indice_primer_espacio:].strip()
    ##Reséndiz Santillan
    indice_espacio = subcad.find(' ')
    apellido_paterno =  subcad[0:indice_espacio]
    print("Apellido Paterno: ", apellido_paterno)
    #Obtener solo el apellido materno
    apellido_materno = subcad[indice_espacio:].strip()
    print("Apellido materno: " , apellido_materno)
    #Obtener las dos primeras letras del apellido paterno
    paterno_dos = apellido_paterno[0:2]
    #Obtener la primer letra del apellido materno
    materno_primera = apellido_materno[0:1]
    #Obtener la primer letra del nombre
    nombre_primera = nombre_usuario[0:1]
    #Extraer los últimos 2 dígitos del año de la fecha
    dos_anio = fecha[-2:]
    #Extraer los 2 dígitos del mes de la fecha
    dos_mes =  fecha[3:5]
    #Extraer los 2 dígitos del día
    dos_dia = fecha[0:2]
    #Concatenar para formar el RFC 
    rfc = paterno_dos + materno_primera + nombre_primera + dos_anio + dos_mes + dos_dia
    #Mostrar el RFC en formato cadena
    print(rfc.upper())
    

    
    
