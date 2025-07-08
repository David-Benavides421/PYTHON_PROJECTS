from pymongo import MongoClient

cliente = MongoClient("mongodb+srv://fullsena:Sena2025@servidorfull.vdfoqwj.mongodb.net/?retryWrites=true&w=majority&appName=SERVIDORFULL")
db = cliente["agenda_contactos"]
coleccion = db["contactos"]

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }
    coleccion.insert_one(contacto)
    print("Contacto agregado.")

def buscar_contacto():
    nombre = input("Nombre a buscar: ")
    contacto = coleccion.find_one({"nombre": nombre})
    if contacto:
        print(f"Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
    else:
        print("Contacto no encontrado.")

def editar_contacto():
    nombre = input("Nombre a editar: ")
    contacto = coleccion.find_one({"nombre": nombre})
    if contacto:
        nuevo_telefono = input("Nuevo teléfono: ")
        nuevo_correo = input("Nuevo correo: ")
        coleccion.update_one(
            {"nombre": nombre},
            {"$set": {"telefono": nuevo_telefono, "correo": nuevo_correo}}
        )
        print("Contacto actualizado.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Nombre a eliminar: ")
    resultado = coleccion.delete_one({"nombre": nombre})
    if resultado.deleted_count > 0:
        print("Contacto eliminado.")
    else:
        print("Contacto no encontrado.")

# Menú principal 
while True:
    print("\nAgenda de Contactos")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Editar contacto")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        editar_contacto()
    elif opcion == "5":
        print("Saliendo de la agenda.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
