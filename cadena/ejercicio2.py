# Realizar un programa que comprueba si una cadena leida por teclado comienza por una subcadena introduciad por teclado 

cad = input("Introduce una cadena:")
sudcad = input("Introduce una subcadena:")
if cad.startswith(sudcad):
    print("La cadena comienza por la subcadena")
else:
    print("La cadena no comienza por la subcadena")