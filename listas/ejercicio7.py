# Programa que declaro tres listas 'lista1', 'lista2',
# enteros de cada uno, pida valores para 
#calcule lista3=lista1+lista2.

lista1 = []
lista2 = []
lista3 = []

for indice in range(1,6):
    lista1.append(int(input("introduce el elemento %d del vector1: " % indice)))
for indice in range(1,6):
    lista2.append(int(input("introduce el elemento %d del vector2: " % indice)))

for indice in range(0,5):
    lista3.append(lista1[indice] + lista2[indice])

print("la suma de los vectores es:")
for numero in lista3:
    print(numero, " ", end="") 