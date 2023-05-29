import tkinter as tk
import sqlite3

def mostrar_farmacos():
    conn = sqlite3.connect('nombres.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM farmacos")
    resultados = cursor.fetchall()
    conn.close()

    # Limpiar resultados anteriores en la lista
    lista_farmacos.delete(0, tk.END)

    # Mostrar los fármacos en la lista
    for row in resultados:
        lista_farmacos.insert(tk.END, f"ID: {row[0]}, Nombre: {row[1]}, Precio: {row[2]}")

def insertar_farmaco():
    nombre = entry_nombre.get()
    precio = float(entry_precio.get())

    conn = sqlite3.connect('nombres.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO farmacos (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conn.commit()
    conn.close()

    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

    mostrar_farmacos()

def eliminar_farmaco():
    id_farmaco = int(entry_id.get())

    conn = sqlite3.connect('nombres.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM farmacos WHERE id = ?", (id_farmaco,))
    conn.commit()
    conn.close()

    entry_id.delete(0, tk.END)

    mostrar_farmacos()

def editar_farmaco():
    id_farmaco = int(entry_id.get())
    nuevo_nombre = entry_nombre.get()
    nuevo_precio = float(entry_precio.get())

    conn = sqlite3.connect('nombres.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE farmacos SET nombre = ?, precio = ? WHERE id = ?", (nuevo_nombre, nuevo_precio, id_farmaco))
    conn.commit()
    conn.close()

    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

    mostrar_farmacos()

# Crear la ventana de la interfaz
ventana = tk.Tk()
ventana.title("Farmacia")

# Etiquetas
label_id = tk.Label(ventana, text="ID del fármaco:")
label_id.grid(row=0, column=0, padx=5, pady=5)

label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=1, column=0, padx=5, pady=5)

label_precio = tk.Label(ventana, text="Precio:")
label_precio.grid(row=2, column=0, padx=5, pady=5)

# Campos de entrada
entry_id = tk.Entry(ventana)
entry_id.grid(row=0, column=1, padx=5, pady=5)

entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1, column=1, padx=5, pady=5)

entry_precio = tk.Entry(ventana)
entry_precio.grid(row=2, column=1, padx=5, pady=5)

# Botones
boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_farmacos)
boton_mostrar.grid(row=3, column=0, padx=5, pady=5)

boton_insertar = tk.Button(ventana, text="Insertar", command=insertar_farmaco)
boton_insertar.grid(row=3, column=1, padx=5, pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_farmaco)
boton_eliminar.grid(row=4, column=0, padx=5, pady=5)

boton_editar = tk.Button(ventana, text="Editar", command=editar_farmaco)
boton_editar.grid(row=4, column=1, padx=5, pady=5)

# Lista de fármacos
lista_farmacos = tk.Listbox(ventana)
lista_farmacos.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Configuración de la lista de fármacos
scrollbar = tk.Scrollbar(ventana)
scrollbar.grid(row=5, column=2, sticky="ns")
lista_farmacos.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_farmacos.yview)

# Ejecutar la interfaz gráfica
ventana.mainloop()
