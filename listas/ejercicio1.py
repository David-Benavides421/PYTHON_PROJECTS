# Realiza que inicialize una lista con 10 numeros aleatorios entre 1 y 10.
# Y muestre cada elemento con su cuadro y su cubo

import random 
lista_numeros = []

for i in range(1,11):
    lista_numeros.append(random.randint(1,10))

for numero in lista_numeros:
    print(numero, " ",numero ** 2, " ", numero ** 3)