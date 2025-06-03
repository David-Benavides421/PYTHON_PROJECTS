#introduccir una cadena de caracteres e indicar si es palindromo. una palabra
# palidroma es aquella que se lee igual adelante que atras

cad = input("Introduce una cadena:")
if cad == cad[::-1].lower():
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")