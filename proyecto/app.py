from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Conexión a MongoDB
cliente = MongoClient("mongodb+srv://fullsena:Sena2025@servidorfull.vdfoqwj.mongodb.net/?retryWrites=true&w=majority&appName=SERVIDORFULL")
db = cliente["agenda_contactos"]
coleccion = db["contactos"]

# Ruta para agregar un contacto
@app.route('/contactos', methods=['POST'])
def agregar_contacto():
    data = request.get_json()
    nombre = data.get("nombre")
    telefono = data.get("telefono")
    correo = data.get("correo")
    
    if not nombre or not telefono or not correo:
        return jsonify({"mensaje": "Faltan datos"}), 400
    
    coleccion.insert_one({"nombre": nombre, "telefono": telefono, "correo": correo})
    return jsonify({"mensaje": "Contacto agregado"}), 200

# Ruta para buscar contacto
@app.route('/contactos/<nombre>', methods=['GET'])
def buscar_contacto(nombre):
    contacto = coleccion.find_one({"nombre": nombre})
    if contacto:
        return jsonify({
            "telefono": contacto["telefono"],
            "correo": contacto["correo"]
        }), 200
    return jsonify({"mensaje": "No encontrado"}), 404

# Ruta para editar contacto
@app.route('/contactos/<nombre>', methods=['PUT'])
def editar_contacto(nombre):
    data = request.get_json()
    telefono = data.get("telefono")
    correo = data.get("correo")
    
    result = coleccion.update_one(
        {"nombre": nombre},
        {"$set": {"telefono": telefono, "correo": correo}}
    )
    if result.modified_count > 0:
        return jsonify({"mensaje": "Contacto actualizado"}), 200
    return jsonify({"mensaje": "No encontrado o sin cambios"}), 404

# Ruta para eliminar contacto
@app.route('/contactos/<nombre>', methods=['DELETE'])
def eliminar_contacto(nombre):
    result = coleccion.delete_one({"nombre": nombre})
    if result.deleted_count > 0:
        return jsonify({"mensaje": "Contacto eliminado"}), 200
    return jsonify({"mensaje": "No encontrado"}), 404

if __name__ == '_main_':
    app.run(debug=True)