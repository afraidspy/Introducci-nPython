file_handler = open('ejemplo.txt', 'r')

count = 0


for line in file_handler:


    count = count + 1


print('Número total de líneas:', count)


file_handler.close() 


opt = 'a'


file_handler = open('prueba.txt', opt)
