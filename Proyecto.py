import sqlite3

def mostrar_farmacos():
    # Establecer conexión con la base de datos
    conn = sqlite3.connect('nombres.db')

    # Crear cursor
    cursor = conn.cursor()

    # Obtener los fármacos de la tabla
    cursor.execute("SELECT * FROM farmacos")

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Mostrar los fármacos
    for row in resultados:
        print(f"ID: {row[0]}, Nombre: {row[1]}, Precio: {row[2]}")

    # Cerrar conexión
    conn.close()

def insertar_farmaco():
    # Establecer conexión con la base de datos
    conn = sqlite3.connect('nombres.db')

    # Crear cursor
    cursor = conn.cursor()

    # Solicitar datos del fármaco al usuario
    nombre = input("Ingrese el nombre del fármaco: ")
    precio = float(input("Ingrese el precio del fármaco: "))

    # Insertar fármaco en la tabla
    cursor.execute("INSERT INTO farmacos (nombre, precio) VALUES (?, ?)", (nombre, precio))

    # Guardar cambios
    conn.commit()

    print("Fármaco insertado correctamente.")

    # Cerrar conexión
    conn.close()

def eliminar_farmaco():
    # Establecer conexión con la base de datos
    conn = sqlite3.connect('nombres.db')

    # Crear cursor
    cursor = conn.cursor()

    # Solicitar ID del fármaco a eliminar
    id_farmaco = int(input("Ingrese el ID del fármaco a eliminar: "))

    # Eliminar fármaco de la tabla
    cursor.execute("DELETE FROM farmacos WHERE id = ?", (id_farmaco,))

    # Guardar cambios
    conn.commit()

    print("Fármaco eliminado correctamente.")

    # Cerrar conexión
    conn.close()

# Solicitar opción al usuario
opcion = input("Seleccione una opción:\n1. Mostrar fármacos\n2. Insertar fármaco\n3. Eliminar fármaco\nOpción a seleccionar: \n")

if opcion == "1":
    mostrar_farmacos()
elif opcion == "2":
    insertar_farmaco()
elif opcion == "3":
    eliminar_farmaco()
else:
    print("Opción inválida")
