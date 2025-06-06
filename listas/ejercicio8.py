# Queremos guardar los nombres y la edades de los alunmos de un curso 
# Realiza un programa que introduzca el nombre y edad de cada alunmo
# El proceso de lectura de datos terminara cuando se introduzca como nombre
# un asterisco (*) al finalizar se mostrara los sigientes los siguientes datos:
# * Todos lo alumno mayores de edad
# * Los alunmos mayores (los que tienen mas edad)

nombres = []
edades = []
# inicializo las listas hasta que introduzca un "*"

while True:
    nombre = input("Dime el nombre de un alunmo: ")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime su edad:")))