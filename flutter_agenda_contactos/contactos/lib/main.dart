import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() => runApp(const MyApp());

const apiUrl =
    "http://127.0.0.1:5000/contactos"; // Cambia esta URL según tu entorno

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Agenda de Contactos',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.indigo),
        useMaterial3: true,
      ),
      home: const ContactosPage(),
    );
  }
}

class ContactosPage extends StatefulWidget {
  const ContactosPage({super.key});
  @override
  State<ContactosPage> createState() => _ContactosPageState();
}

class _ContactosPageState extends State<ContactosPage> {
  final nombreCtrl = TextEditingController();
  final telefonoCtrl = TextEditingController();
  final correoCtrl = TextEditingController();
  String mensaje = '';

  Future<void> agregarContacto() async {
    final res = await http.post(
      Uri.parse(apiUrl),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "nombre": nombreCtrl.text,
        "telefono": telefonoCtrl.text,
        "correo": correoCtrl.text,
      }),
    );
    setState(() => mensaje = jsonDecode(res.body)['mensaje'] ?? 'Agregado');
  }

  Future<void> buscarContacto() async {
    final res = await http.get(Uri.parse("$apiUrl/${nombreCtrl.text}"));
    if (res.statusCode == 200) {
      final data = jsonDecode(res.body);
      telefonoCtrl.text = data["telefono"];
      correoCtrl.text = data["correo"];
      setState(() => mensaje = "Contacto encontrado.");
    } else {
      setState(() => mensaje = "No encontrado.");
    }
  }

  Future<void> editarContacto() async {
    final res = await http.put(
      Uri.parse("$apiUrl/${nombreCtrl.text}"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "telefono": telefonoCtrl.text,
        "correo": correoCtrl.text,
      }),
    );
    setState(() => mensaje = jsonDecode(res.body)['mensaje'] ?? 'Editado');
  }

  Future<void> eliminarContacto() async {
    final res = await http.delete(Uri.parse("$apiUrl/${nombreCtrl.text}"));
    setState(() => mensaje = jsonDecode(res.body)['mensaje'] ?? 'Eliminado');
    telefonoCtrl.clear();
    correoCtrl.clear();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Agenda de Contactos'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Card(
          elevation: 6,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
          ),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                const Text(
                  'Gestión de Contactos',
                  style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 20),
                TextField(
                  controller: nombreCtrl,
                  decoration: const InputDecoration(
                    labelText: 'Nombre',
                    border: OutlineInputBorder(),
                  ),
                ),
                const SizedBox(height: 10),
                TextField(
                  controller: telefonoCtrl,
                  decoration: const InputDecoration(
                    labelText: 'Teléfono',
                    border: OutlineInputBorder(),
                  ),
                ),
                const SizedBox(height: 10),
                TextField(
                  controller: correoCtrl,
                  decoration: const InputDecoration(
                    labelText: 'Correo',
                    border: OutlineInputBorder(),
                  ),
                ),
                const SizedBox(height: 20),
                Wrap(
                  spacing: 12,
                  children: [
                    ElevatedButton(
                      onPressed: agregarContacto,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.green,
                      ),
                      child: const Text("Agregar"),
                    ),
                    ElevatedButton(
                      onPressed: buscarContacto,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.blue,
                      ),
                      child: const Text("Buscar"),
                    ),
                    ElevatedButton(
                      onPressed: editarContacto,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.orange,
                      ),
                      child: const Text("Editar"),
                    ),
                    ElevatedButton(
                      onPressed: eliminarContacto,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.red,
                      ),
                      child: const Text("Eliminar"),
                    ),
                  ],
                ),
                const SizedBox(height: 20),
                Text(
                  mensaje,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}