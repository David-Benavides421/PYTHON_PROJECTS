
frutas = {'platano' : 1.35,
        'manzana' : 0.8,
        'pera' : 2000,
        'naranja' : 0.7}

fruta = input("que fruta deseas comprar ?").lower()
kg = float(input("Introduce el numero de kilos que vas a comprar: "))

if fruta in frutas:
    precio = frutas[fruta] *kg
    print(f"El precio de {kg} kilos de {fruta} es: {precio}")
else:
    print("La fruta que ingresaste no esta disponible")
