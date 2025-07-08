nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
direccion = input('Ingrese su dirección: ')
telefono = input('Ingrese su teléfono: ')

persona = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono}

print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])