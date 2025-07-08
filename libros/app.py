from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)

# Conexión MongoDB
cliente = MongoClient("mongodb+srv://fullsena:Sena2025@servidorfull.vdfoqwj.mongodb.net/?retryWrites=true&w=majority&appName=SERVIDORFULL")
db = cliente["agenda_contactos"]
coleccion = db["libros"]

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        titulo = request.form['titulo']
        autor = request.form['autor']
        editorial = request.form['editorial']
        anio = request.form['anio']
        isbn = request.form['ISBN']
        ubicacion = request.form['ubicacion']
        estado = request.form['estado']
        accion = request.form['accion']

        if accion == 'Agregar':
            coleccion.insert_one({"titulo": titulo, "autor": autor, "editorial": editorial, "anio": anio, "ISBN": isbn, "ubicacion": ubicacion, "estado": estado})
            mensaje = "Contacto agregado."
        elif accion == 'Buscar':
            contacto = coleccion.find_one({"titulo": titulo})
            if contacto:
                telefono = contacto['telefono']
                correo = contacto['correo']
                mensaje = "Contacto encontrado."
            else:
                mensaje = "No encontrado."
        elif accion == 'Editar':
            coleccion.update_one({"titulo": titulo}, {"$set": {"editorial": editorial, "anio": anio, "ISBN": isbn, "ubicacion": ubicacion, "estado": estado}})
            mensaje = "Contacto actualizado."
        elif accion == 'Eliminar':
            coleccion.delete_one({"titulo": titulo})
            mensaje = "Contacto eliminado."

    return render_template("index.html", mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
    



"""mongodb+srv://fullsena:Sena2025@servidorfull.vdfoqwj.mongodb.net/?retryWrites=true&w=majority&appName=SERVIDORFULL"""
"""
from flask import Flask, render_template, request
from pymongo import MongoClient
import re # Importamos la librería para expresiones regulares

app = Flask(__name__)

# --- Conexión MongoDB ---
# Asegúrate de que tu IP esté en la lista blanca de MongoDB Atlas
# y que el usuario/contraseña sean correctos.
try:
    cliente = MongoClient("mongodb+srv://fullsena:Sena2025@servidorfull.vdfoqwj.mongodb.net/?retryWrites=true&w=majority&appName=SERVIDORFULL", serverSelectionTimeoutMS=5000)
    # La siguiente línea prueba la conexión. Si falla, lanzará una excepción.
    cliente.server_info() 
    print("✅ Conexión a MongoDB exitosa.")
except Exception as e:
    print(f"❌ Error al conectar a MongoDB: {e}")
    # Si hay un error aquí, la aplicación no funcionará.
    
db = cliente["agenda_contactos"]
coleccion = db["libros"]

@app.route("/", methods=["GET", "POST"])
def index():
    print("\n--- Nueva Petición Recibida ---")
    mensaje = ""
    libro_encontrado = None

    if request.method == "POST":
        print("Petición de tipo POST detectada.")
        
        # Obtenemos los datos del formulario
        accion = request.form.get('accion')
        titulo = request.form.get('titulo')
        
        print(f"➡️  Acción recibida: '{accion}'")
        print(f"➡️  Título recibido: '{titulo}'")

        if not titulo and accion in ['Buscar', 'Editar', 'Eliminar']:
            mensaje = "Error: El campo 'Título' es necesario para buscar, editar o eliminar."
            return render_template("index.html", mensaje=mensaje, libro=None)

        # Usamos .get() para evitar errores si un campo viene vacío
        autor = request.form.get('autor')
        editorial = request.form.get('editorial')
        anio = request.form.get('anio')
        isbn = request.form.get('ISBN')
        ubicacion = request.form.get('ubicacion')
        estado = request.form.get('estado')

        if accion == 'Agregar':
            print("Ejecutando lógica de 'Agregar'...")
            # Comprobamos si ya existe para no duplicar
            if coleccion.find_one({"titulo": titulo}):
                mensaje = f"Error: Ya existe un libro con el título '{titulo}'."
                print(f"Intento de agregar libro duplicado: '{titulo}'")
            else:
                libro_nuevo = {"titulo": titulo, "autor": autor, "editorial": editorial, "anio": anio, "ISBN": isbn, "ubicacion": ubicacion, "estado": estado}
                coleccion.insert_one(libro_nuevo)
                mensaje = "Libro agregado correctamente."
                print(f"✅ Libro agregado a la DB: {libro_nuevo}")

        elif accion == 'Buscar':
            print(f"Ejecutando lógica de 'Buscar' para el título: '{titulo}'")
            # Búsqueda insensible a mayúsculas/minúsculas para mejorar la experiencia
            regex = re.compile(f'^{re.escape(titulo)}$', re.IGNORECASE)
            libro_encontrado = coleccion.find_one({"titulo": regex})
            
            print(f"🔎 Resultado de la búsqueda en DB: {libro_encontrado}")

            if libro_encontrado:
                mensaje = "Libro encontrado. Sus datos han sido cargados."
            else:
                mensaje = f"No se encontró ningún libro con el título '{titulo}'."

        elif accion == 'Editar':
            print(f"Ejecutando lógica de 'Editar' para el título: '{titulo}'")
            resultado = coleccion.update_one(
                {"titulo": titulo}, 
                {"$set": {"autor": autor, "editorial": editorial, "anio": anio, "ISBN": isbn, "ubicacion": ubicacion, "estado": estado}}
            )
            if resultado.modified_count > 0:
                mensaje = "Libro actualizado correctamente."
                print(f"✅ Libro '{titulo}' actualizado en la DB.")
            else:
                mensaje = "No se encontró un libro con ese título para actualizar o no hubo cambios."
                print(f"⚠️ No se pudo actualizar '{titulo}'. No se encontró o no hubo cambios.")

        elif accion == 'Eliminar':
            print(f"Ejecutando lógica de 'Eliminar' para el título: '{titulo}'")
            resultado = coleccion.delete_one({"titulo": titulo})
            if resultado.deleted_count > 0:
                mensaje = "Libro eliminado correctamente."
                print(f"✅ Libro '{titulo}' eliminado de la DB.")
            else:
                mensaje = "No se encontró ningún libro con ese título para eliminar."
                print(f"⚠️ No se pudo eliminar '{titulo}'. No se encontró.")

    else:
        print("Petición de tipo GET detectada (primera carga de la página).")

    print(f"✔️  Renderizando plantilla con mensaje: '{mensaje}'")
    print(f"✔️  Datos del libro pasados a la plantilla: {libro_encontrado}")
    return render_template("index.html", mensaje=mensaje, libro=libro_encontrado)

if __name__ == '__main__':
    app.run(debug=True)

    """