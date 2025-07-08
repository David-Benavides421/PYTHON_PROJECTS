import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Conexión MongoDB Atlas
cliente = MongoClient("mongodb+srv://fullsena:Sena2025@servidorfull.vdfoqwj.mongodb.net/?retryWrites=true&w=majority&appName=SERVIDORFULL")
db = cliente['agenda_contactos']
coleccion = db["contactos"]

def agregar_contacto():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    if nombre:
        coleccion.insert_one({"nombre": nombre, "telefono": telefono, "correo": correo})
        messagebox.showinfo("Exito", "Contacto agregado.")
    else:
        messagebox.showwarning("Error", "El nombre es obligatorio.")

def buscar_contacto():
    nombre = entry_nombre.get()
    contacto = coleccion.find_one({"nombre": nombre})
    if contacto:
        entry_telefono.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_telefono.insert(0, contacto['telefono'])
        entry_correo.insert(0, contacto['correo'])
    else:
        messagebox.showwarning("No encontrado", "No se encontró el contacto.")

def editar_contacto():
    nombre = entry_nombre.get()
    if coleccion.find_one({"nombre": nombre}):
        coleccion.update_one(
            {"nombre": nombre},
            {"$set": {"telefono": entry_telefono.get(), "correo": entry_correo.get()}}
        )
        messagebox.showinfo("Actualizado", "Contacto actualizado.")
    else:
        messagebox.showwarning("No encontrado", "No se encontró el contacto.")

def eliminar_contacto():
    nombre = entry_nombre.get()
    result = coleccion.delete_one({"nombre": nombre})
    if result.deleted_count:
        entry_telefono.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        messagebox.showinfo("eliminado", "contacto eliminado.")
    else:
        messagebox.showwarning("No encontrado", "No se encontró el contacto.")

# GUI
ventana = tk.Tk()
ventana.title("Agenda de Contactos")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
tk.Label(ventana, text="Teléfono:").grid(row=1, column=0)
tk.Label(ventana, text="Correo:").grid(row=2, column=0)

entry_nombre = tk.Entry(ventana)
entry_telefono = tk.Entry(ventana)
entry_correo = tk.Entry(ventana)

entry_nombre.grid(row=0, column=1)
entry_telefono.grid(row=1, column=1)
entry_correo.grid(row=2, column=1)

tk.Button(ventana, text="Agregar", command=agregar_contacto).grid(row=3, column=0)
tk.Button(ventana, text="Buscar", command=buscar_contacto).grid(row=3, column=1)
tk.Button(ventana, text="Editar", command=editar_contacto).grid(row=4, column=0)
tk.Button(ventana, text="Eliminar", command=eliminar_contacto).grid(row=4, column=1)

ventana.mainloop()