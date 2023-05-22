'''
Programa para conocer: 
¿Cuál es la edad promedio de los pacientes? y si
¿Hay más hombres o mujeres contagiados?
'''

def get_information():
    '''
    Obtención de la información pedida, al procesar
    el archivo
    '''
    is_first = True
    average = 0.0
    count_man = 0
    count_woman = 0
    sum_age = 0

    for line in file_csv:
        if not is_first:
            data = line.split(',')
            gender = data[2]
            #print('gender..',gender)
            age = data[3]
            if (age != 'NA' and gender != 'NA'):
                sum_age+= int(age)
                if gender == 'FEMENINO':
                    #print("woman")
                    count_woman += 1
                if gender == 'MASCULINO':
                    #print("men")
                    count_man += 1
        else:
            is_first = False

            
            
    total = count_man + count_woman
    #Realizando cálculos
    average = get_average (sum_age, total)
    print('Edad promedio de los pacientes: ', average)
    get_contagiados(count_man, count_woman)


def get_average(sum, total_people):
    '''
    Obtener el promedio de edades, regresando la edad cuyo tipo es entero
    '''
    return sum // total_people

def get_contagiados(count_man, count_woman):
    '''
    Imprime cuál fue el género con más contagios
    '''
    if (count_man > count_woman):
        print ('Hay más hombres contagiados')
    elif (count_woman > count_man ):
        print ('Hay más mujeres contagiadas')
    else:
        print ('La cantidad de hombres y mujeres contagid@s es igual')


if __name__ == "__main__":
    try:
        file_csv = open('casos_confirmados.csv')
        get_information()
        file_csv.close()
    except  FileNotFoundError:
        print("El archivo no se encontrò")
