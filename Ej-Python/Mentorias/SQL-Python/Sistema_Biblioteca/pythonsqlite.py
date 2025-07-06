import sqlite3
import uuid
import datetime

conn = sqlite3.connect("biblioteca.db") #llamamos al modulo

cursor = conn.cursor() #permite interactuar con la base de datos

def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS socios (
            uuid_socio VARCHAR PRIMARY KEY,
            nombre VARCHAR,
            dni INTEGER UNIQUE
            )
        ''') #permite ejecutar el codigo que escribamos como sentencia sql

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            uuid_libro VARCHAR PRIMARY KEY,
            titulo VARCHAR UNIQUE NOT NULL,
            autor VARCHAR,
            categoria INTEGER
            )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS retiros (
            uuid_retiro VARCHAR PRIMARY KEY,
            uuid_socio VARCHAR,
            uuid_libro VARCHAR,
            FOREIGN KEY(uuid_socio) REFERENCES socios(uuid_socio)
            FOREIGN KEY(uuid_libro) REFERENCES libros(uuid_libro)
            )
        ''')

    conn.commit()

def cerrar_conexion():
    cursor.close()
    conn.close()

def insertar_socios():
    uuid_socio = str(uuid.uuid4()) #str(llamamos al modulo y luego seleccionamos uuid4)
    nombre = input("Nombre completo: ")
    dni = input("DNI: ")

    query = '''INSERT INTO socios(uuid_socio, nombre, dni)
    VALUES (?, ?, ?)
    '''#no debemos pasar por aca los valores pq es inseguro, sino dejamos signos de preguntas

    cursor.execute(query, (uuid_socio, nombre, dni))#query - lo toma como tupla
    conn.commit()
    print("El socio se registro exitosamente.")

def insertar_libros():
    uuid_libro = str(uuid.uuid4()) #str(llamamos al modulo y luego seleccionamos uuid4)
    titulo = input("Nombre del libro: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")

    query = '''INSERT INTO libros (uuid_libro, titulo, autor, categoria)
    VALUES (?, ?, ?, ?)
    '''#no debemos pasar por aca los valores pq es inseguro, sino dejamos signos de preguntas

    cursor.execute(query, (uuid_libro, titulo, autor, categoria))#query - lo toma como tupla
    conn.commit()
    print("El libro se registro exitosamente.")

def retiros():
    uuid_retiro = str(uuid.uuid4())

    listar_socios()
    uuid_socio = input("UUID del socio que retira: ")

    listar_libros()
    uuid_libro = input("UUID del libro que se retira: ")

    query = '''INSERT INTO retiros(uuid_retiro, uuid_socio, uuid_libro)
    VALUES (?, ?, ?)
    '''
    cursor.execute(query, (uuid_retiro, uuid_socio, uuid_libro))#query - lo toma como tupla
    conn.commit()
    print("Se registro exitosamente el retiro de un libro por uno de los socios.")

def listar_socios():
    cursor.execute("SELECT * FROM socios") #consulta la consola 
    socios = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for s in socios:
        print(s)

def listar_libros():
    cursor.execute("SELECT * FROM libros") #consulta la consola 
    libros = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for l in libros:
        print(l)

def listar_retiros():
    cursor.execute("SELECT * FROM retiros ") #consulta la consola 
    retiros = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for r in retiros:
        print(r)

def menu():
    crear_tablas()
    while True:
        print("\nMenu")
        print("1. Insertar un socio")
        print("2. Insertar un libro")
        print("3. Registrar un retiro")
        print("4. Listar socios")
        print("5. Listar libros")
        print("6. Listar los retiros")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar_socios()
        elif opcion == "2":
            insertar_libros()
        elif opcion == "3":
            retiros()
        elif opcion == "4":
            listar_socios()
        elif opcion == "5":
            listar_libros()
        elif opcion == "6":
            listar_libros()
        elif opcion == "0":
            cerrar_conexion()
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu()