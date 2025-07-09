from flask import Flask, render_template, request
from pymongo import MongoClient
import re  # Necesario para búsquedas insensibles a mayúsculas/minúsculas

app = Flask(__name__)

# --- Conexión a MongoDB ---
# Es una buena práctica manejar posibles errores de conexión.
try:
    cliente = MongoClient(
        "mongodb+srv://fullsena:Sena2025@servidorfull.vdfoqwj.mongodb.net/?retryWrites=true&w=majority&appName=SERVIDORFULL",
        serverSelectionTimeoutMS=5000 # Tiempo de espera para la conexión
    )
    # Verificamos que la conexión sea exitosa
    cliente.server_info()
    print("✅ Conexión a MongoDB exitosa.")
except Exception as e:
    print(f"❌ Error al conectar a MongoDB. La aplicación no podrá funcionar. Error: {e}")
    # En un caso real, podrías querer que la aplicación se detenga si no hay BD.

db = cliente["agenda_contactos"]
coleccion = db["libros"]

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    libro_encontrado = None  # Variable para pasar los datos al HTML

    if request.method == "POST":
        # Usamos .get() para evitar errores si un campo está ausente
        accion = request.form.get('accion')
        titulo = request.form.get('titulo', '').strip() # .strip() elimina espacios en blanco

        # Si la acción requiere un título y no se proporciona, mostramos un error.
        if not titulo and accion in ['Buscar', 'Editar', 'Eliminar']:
            mensaje = "Error: Se necesita un título para Buscar, Editar o Eliminar."
            return render_template("index.html", mensaje=mensaje, libro=None)

        # Obtenemos el resto de los datos del formulario
        autor = request.form.get('autor')
        editorial = request.form.get('editorial')
        anio = request.form.get('anio')
        isbn = request.form.get('ISBN')
        ubicacion = request.form.get('ubicacion')
        estado = request.form.get('estado')

        if accion == 'Agregar':
            # Verificamos que al menos el título, autor e ISBN existan
            if titulo and autor and isbn:
                # Comprobamos si ya existe para no duplicar
                if coleccion.find_one({"titulo": titulo}):
                    mensaje = f"Error: Ya existe un libro con el título '{titulo}'."
                else:
                    nuevo_libro = {
                        "titulo": titulo, "autor": autor, "editorial": editorial,
                        "anio": anio, "ISBN": isbn, "ubicacion": ubicacion, "estado": estado
                    }
                    coleccion.insert_one(nuevo_libro)
                    mensaje = "Libro agregado correctamente."
            else:
                mensaje = "Error: Título, Autor e ISBN son campos requeridos para agregar."

        elif accion == 'Buscar':
            # Búsqueda insensible a mayúsculas/minúsculas para mejor usabilidad
            regex = re.compile(f'^{re.escape(titulo)}$', re.IGNORECASE)
            libro_encontrado = coleccion.find_one({"titulo": regex})
            if libro_encontrado:
                mensaje = "Libro encontrado. Sus datos han sido cargados en el formulario."
            else:
                mensaje = f"No se encontró ningún libro con el título '{titulo}'."

        elif accion == 'Editar':
            # Actualizamos el libro usando el título como identificador
            resultado = coleccion.update_one(
                {"titulo": titulo},
                {"$set": {
                    "autor": autor, "editorial": editorial, "anio": anio,
                    "ISBN": isbn, "ubicacion": ubicacion, "estado": estado
                }}
            )
            if resultado.modified_count > 0:
                mensaje = "Libro actualizado correctamente."
                # Después de editar, volvemos a buscar para mostrar los datos actualizados
                libro_encontrado = coleccion.find_one({"titulo": titulo})
            else:
                mensaje = "No se encontró un libro con ese título o no hubo cambios para actualizar."
                libro_encontrado = coleccion.find_one({"titulo": titulo}) # Mostramos los datos aunque no se hayan cambiado

        elif accion == 'Eliminar':
            resultado = coleccion.delete_one({"titulo": titulo})
            if resultado.deleted_count > 0:
                mensaje = "Libro eliminado correctamente."
                # No pasamos libro_encontrado porque ya no existe
            else:
                mensaje = "No se encontró ningún libro con ese título para eliminar."

    # Pasamos el mensaje y el libro_encontrado a la plantilla
    # Si no se encontró un libro, la variable libro_encontrado será None
    return render_template("index.html", mensaje=mensaje, libro=libro_encontrado)

if __name__ == '__main__':
    app.run(debug=True)