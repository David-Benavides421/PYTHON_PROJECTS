import random
lista = []

for indice in range(1, 11):
    lista.append(random.randint(1, 10))

lista.sort()

for numero in lista:
    print(numero, " ", end="")