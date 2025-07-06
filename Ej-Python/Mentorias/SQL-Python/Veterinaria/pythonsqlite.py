import sqlite3
import uuid
import datetime

conn = sqlite3.connect("veterinaria.db") #llamamos al modulo

cursor = conn.cursor() #permite interactuar con la base de datos

def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS duenos (
            uuid_dueno VARCHAR PRIMARY KEY,
	        nombre VARCHAR,
	        dni INTEGER UNIQUE NOT NULL
            )
        ''') #permite ejecutar el codigo que escribamos como sentencia sql

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mascotas (
	        uuid_mascota VARCHAR PRIMARY KEY,
	        nombre VARCHAR NOT NULL,
	        especie VARCHAR NOT NULL,
	        edad INTEGER NOT NULL
            )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tienen (
            uuid_dueno VARCHAR,
            uuid_mascota VARCHAR,
            FOREIGN KEY(uuid_dueno) REFERENCES duenos(uuid_dueno)
            FOREIGN KEY(uuid_mascota) REFERENCES mascotas(uuid_mascota)
            )
        ''')

    conn.commit()

def cerrar_conexion():
    cursor.close()
    conn.close()

def registrar_duenos():
    uuid_dueno = str(uuid.uuid4()) #str(llamamos al modulo y luego seleccionamos uuid4)
    nombre = input("Nombre completo: ")
    dni = input("DNI: ")

    query = '''INSERT INTO duenos(uuid_dueno, nombre, dni)
    VALUES (?, ?, ?)
    '''#no debemos pasar por aca los valores pq es inseguro, sino dejamos signos de preguntas

    cursor.execute(query, (uuid_dueno, nombre, dni))#query - lo toma como tupla
    conn.commit()
    print("El dueño se registro exitosamente.")

def registrar_mascotas():
    uuid_mascota = str(uuid.uuid4()) #str(llamamos al modulo y luego seleccionamos uuid4)
    nombre = input("Nombre de tu mascota: ")
    especie = input("Que especie es?: ")
    edad = input("Que edad tiene?: ")

    query = '''INSERT INTO mascotas(uuid_mascota, nombre, especie, edad)
    VALUES (?, ?, ?, ?)
    '''#no debemos pasar por aca los valores pq es inseguro, sino dejamos signos de preguntas

    cursor.execute(query, (uuid_mascota, nombre, especie, edad))#query - lo toma como tupla
    conn.commit()
    print("La mascota se registro exitosamente.")

def DuenoTieneMascota():

    listar_duenos()
    uuid_dueno = input("UUID del dueno: ")

    listar_mascotas()
    uuid_mascota = input("UUID de la mascota: ")

    query = '''INSERT INTO tienen(uuid_dueno, uuid_mascota)
    VALUES (?, ?)
    '''
    cursor.execute(query, (uuid_dueno, uuid_mascota))#query - lo toma como tupla
    conn.commit()
    print("El dueño y su mascota estan registrados exitosamente.")

def listar_duenos():
    cursor.execute("SELECT * FROM duenos") #consulta la consola 
    duenos = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for d in duenos:
        print(d)

def listar_mascotas():
    cursor.execute("SELECT * FROM mascotas") #consulta la consola 
    mascotas = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for m in mascotas:
        print(m)

def listar_DuenoTieneMascota():
    cursor.execute("SELECT * FROM tienen") #consulta la consola 
    duenosmascotas = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for dm in duenosmascotas:
        print(dm)

def menu():
    crear_tablas()
    while True:
        print("\nMenu")
        print("1. Registrar dueño")
        print("2. Registrar mascota")
        print("3. Registro de dueños con mascotas")
        print("4. Listar dueño")
        print("5. Listar mascota")
        print("6. Listar dueños con sus mascotas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_duenos()
        elif opcion == "2":
            registrar_mascotas()
        elif opcion == "3":
            DuenoTieneMascota()
        elif opcion == "4":
            listar_duenos()
        elif opcion == "5":
            listar_mascotas()
        elif opcion == "6":
            listar_DuenoTieneMascota()
        elif opcion == "0":
            cerrar_conexion()
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu()