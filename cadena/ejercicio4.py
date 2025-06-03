# Suponiendo que hemos introcudido una cadena por teclado que representa una frase y que contiene varias palabrase 
# (Palabras separadas por espacios), realiza un programa qye cuente cuentas
# palabras tiene.

cont = 0
posicion = 0
cad = input("Introduce una cadena:")
# Elimino los posibles espaciones que haya la principio y final de las cadena
cad = cad.strip()
# voy buscando los espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
    cont += 1
    # Actualizo la posición para buscar el siguiente espacio
    while cad[posicion + 1 ]== " ":
        posicion += 1
    posicion = cad.find(" ", posicion + 1)
print("La frase tiene", cont + 1, "palabras")