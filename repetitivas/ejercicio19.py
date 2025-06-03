#Realizar un ejemplo de menú, donde podemos escoger las distintas opciones:
# que seleccionamos la opcion de "salir".

while True:
    #mostrar menu
    print("Menu de recomendaciones")
    print("1. Literatura")
    print("2. Cine")
    print("3. Música")
    print("4. Videojuegos")
    print("5. Salir")

    #ingresa una opcion
    opcion = input("Selecciona una opción (1-5): ")
    #procesar esa opcion
    if opcion == 1:
        print("Lecturas recomendables: ")
        print("+ Cien años de soledad: ")
        print("+ El coronel no tiene quien le escriba")
        print("+ El quijote")
    elif opcion == 2:
        print("Películas recomendables: ")
        print("+ Matrix(1999)") 
        print("+ El ultimo samuray (2003)")
        print("+ Cars (2006)")
    elif opcion == 3:
        print("Discos recomendables: ")
        print("+ Despedazado por mil partes (La Renga, 1996)")
        print("+ Bufalo(La Misisipi, 2008")
        print("+ Gaia(Mago de Oz, 2003)")
    elif opcion == 4:
        print("Videojuegos recomendables: ")
        print("+ Dia del tentaculo (LucasArts, 1993)")
        print("+ Terminal Velocity (Terminal Really/3D realms, 1995)")
        print("+ Deahth Rally (Remedy Entertainment, 1996)")
    elif opcion == 5:
        print("Gracias, vuelva prontos")
        break
    else:
        print("Opción no válida")