import sqlite3
import uuid
import datetime

conn = sqlite3.connect("alquiler.db") #llamamos al modulo

cursor = conn.cursor() #permite interactuar con la base de datos

def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            uuid_usuario VARCHAR PRIMARY KEY,
            email VARCHAR UNIQUE NOT NULL,
            nombre VARCHAR,
            fecha_nacimiento TIMESTAMP NOT NULL,
            pais VARCHAR
            )
        ''') #permite ejecutar el codigo que escribamos como sentencia sql

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS peliculas (
            uuid_pelicula VARCHAR PRIMARY KEY,
            titulo VARCHAR UNIQUE NOT NULL,
            genero VARCHAR,
            duracion INTEGER
            )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alquileres (
            uuid_alquiler VARCHAR PRIMARY KEY,
            uuid_usuario VARCHAR,
            uuid_pelicula VARCHAR,
            fecha VARCHAR,
            precio REAL,
            tipo_visualizacion VARCHAR NOT NULL,
            FOREIGN KEY(uuid_usuario) REFERENCES usuarios(uuid_usuario)
            FOREIGN KEY(uuid_pelicula) REFERENCES peliculas(uuid_pelicula)
            )
        ''')

    conn.commit()

def cerrar_conexion():
    cursor.close()
    conn.close()

def insertar_usuario():
    uuid_usuario = str(uuid.uuid4()) #str(llamamos al modulo y luego seleccionamos uuid4)
    email = input("Email: ")
    nombre = input("Nombre completo: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY/MM/DD): ")
    pais = input("Pais: ")

    query = '''INSERT INTO usuarios(uuid_usuario, email, nombre, fecha_nacimiento, pais)
    VALUES (?, ?, ?, ?, ?)
    '''#no debemos pasar por aca los valores pq es inseguro, sino dejamos signos de preguntas

    cursor.execute(query, (uuid_usuario, email, nombre, fecha_nacimiento, pais))#query - lo toma como tupla
    conn.commit()
    print("El usuario se registro exitosamente.")

def insertar_peliculas():
    uuid_pelicula = str(uuid.uuid4()) #str(llamamos al modulo y luego seleccionamos uuid4)
    titulo = input("Nombre de la pelicula: ")
    genero = input("Genero de la pelicula: ")
    duracion = input("Duracion: ")

    query = '''INSERT INTO peliculas(uuid_pelicula, titulo, genero, duracion)
    VALUES (?, ?, ?, ?)
    '''#no debemos pasar por aca los valores pq es inseguro, sino dejamos signos de preguntas

    cursor.execute(query, (uuid_pelicula, titulo, genero, duracion))#query - lo toma como tupla
    conn.commit()
    print("La pelicula se registro exitosamente.")

def alquilarUsuarios():
    uuid_alquiler = str(uuid.uuid4())

    listar_usuarios()
    uuid_usuario = input("UUID del usuario que alquila: ")

    listar_peliculas()
    uuid_pelicula = input("UUID de la pelicula que se alquila: ")
    fecha = datetime.datetime.now() #que convierta a string con strftime
    precio = float(input("Precio del alquiler: "))
    tipo_visualizacion = input("Descargada u online: ")

    query = '''INSERT INTO alquileres (uuid_alquiler, uuid_usuario, uuid_pelicula, fecha, precio, tipo_visualizacion)
    VALUES (?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (uuid_alquiler, uuid_usuario, uuid_pelicula, fecha, precio, tipo_visualizacion))#query - lo toma como tupla
    conn.commit()
    print("La pelicula se alquilo exitosamente.")

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios") #consulta la consola 
    usuarios = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for u in usuarios:
        print(u)

def listar_peliculas():
    cursor.execute("SELECT * FROM peliculas") #consulta la consola 
    peliculas = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for p in peliculas:
        print(p)

def listar_alquileres():
    cursor.execute("SELECT * FROM alquileres") #consulta la consola 
    alquileres = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for a in alquileres:
        print(a)

def menu():
    crear_tablas()
    while True:
        print("\nMenu")
        print("1. Insertar un usuario")
        print("2. Insertar una película")
        print("3. Alquilar una película")
        print("4. Listar usuarios")
        print("5. Listar películas")
        print("6. Listar alquileres")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar_usuario()
        elif opcion == "2":
            insertar_peliculas()
        elif opcion == "3":
            alquilarUsuarios()
        elif opcion == "4":
            listar_usuarios()
        elif opcion == "5":
            listar_peliculas()
        elif opcion == "6":
            listar_alquileres()
        elif opcion == "0":
            cerrar_conexion()
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu()