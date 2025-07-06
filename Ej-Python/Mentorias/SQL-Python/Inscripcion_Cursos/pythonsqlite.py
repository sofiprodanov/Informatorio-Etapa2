import sqlite3
import uuid
import datetime

conn = sqlite3.connect("inscripcion_cursos.db") #llamamos al modulo

cursor = conn.cursor() #permite interactuar con la base de datos

def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            uuid_usuario VARCHAR PRIMARY KEY,
            nombre VARCHAR,
            email VARCHAR UNIQUE NOT NULL,
            pais VARCHAR
            )
        ''') #permite ejecutar el codigo que escribamos como sentencia sql

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            uuid_curso VARCHAR PRIMARY KEY,
            titulo VARCHAR NOT NULL,
            categoria VARCHAR,
            duracion_hs INTEGER
            )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inscripciones (
            uuid_inscripcion VARCHAR PRIMARY KEY,
            uuid_usuario VARCHAR,
            uuid_curso VARCHAR,
            fecha_inscripcion VARCHAR,
            medio_pago VARCHAR NOT NULL,
            FOREIGN KEY(uuid_usuario) REFERENCES usuarios(uuid_usuario)
            FOREIGN KEY(uuid_curso) REFERENCES cursos(uuid_curso)
            )
        ''')

    conn.commit()

def cerrar_conexion():
    cursor.close()
    conn.close()

def insertar_usuario():
    uuid_usuario = str(uuid.uuid4()) #str(llamamos al modulo y luego seleccionamos uuid4)
    nombre = input("Nombre completo: ")
    email = input("Email: ")
    pais = input("Pais: ")

    query = '''INSERT INTO usuarios(uuid_usuario, nombre, email, pais)
    VALUES (?, ?, ?, ?)
    '''#no debemos pasar por aca los valores pq es inseguro, sino dejamos signos de preguntas

    cursor.execute(query, (uuid_usuario, nombre, email, pais))#query - lo toma como tupla
    conn.commit()
    print("El usuario se registro exitosamente.")

def insertar_cursos():
    uuid_curso = str(uuid.uuid4()) #str(llamamos al modulo y luego seleccionamos uuid4)
    titulo = input("Que curso vas a tomar?: ")
    categoria = input("Dentro de que categoria se encuentra?: ")
    duracion_hs = input("Duracion del curso: ")

    query = '''INSERT INTO cursos(uuid_curso, titulo, categoria, duracion_hs)
    VALUES (?, ?, ?, ?)
    '''#no debemos pasar por aca los valores pq es inseguro, sino dejamos signos de preguntas

    cursor.execute(query, (uuid_curso, titulo, categoria, duracion_hs))#query - lo toma como tupla
    conn.commit()
    print("El curso se registro exitosamente.")

def inscripcion():
    uuid_inscripcion = str(uuid.uuid4())

    listar_usuarios()
    uuid_usuario = input("UUID del usuario a inscribir: ")

    listar_cursos()
    uuid_curso = input("UUID del curso al que se quiere inscribir: ")
    fecha_inscripcion = datetime.datetime.now() #que convierta a string con strftime
    medio_pago = input("Transferencia o tarjeta de credito?: ")

    query = '''INSERT INTO inscripciones(uuid_inscripcion, uuid_usuario, uuid_curso, fecha_inscripcion, medio_pago)
    VALUES (?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (uuid_inscripcion, uuid_usuario, uuid_curso, fecha_inscripcion, medio_pago))#query - lo toma como tupla
    conn.commit()
    print("La usuario se inscribio exitosamente.")

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios") #consulta la consola 
    usuarios = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for u in usuarios:
        print(u)

def listar_cursos():
    cursor.execute("SELECT * FROM cursos") #consulta la consola 
    cursos = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for c in cursos:
        print(c)

def listar_inscripciones():
    cursor.execute("SELECT * FROM inscripciones") #consulta la consola 
    inscripciones = cursor.fetchall() #recupera los resultados de la consulta anterior y las guarda dentro de la variable usuarios y los pasa como tupla
    for i in inscripciones:
        print(i)

def menu():
    crear_tablas()
    while True:
        print("\nMenu")
        print("1. Insertar un usuario")
        print("2. Insertar un curso")
        print("3. Inscribir")
        print("4. Listar usuarios")
        print("5. Listar películas")
        print("6. Listar inscripciones")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar_usuario()
        elif opcion == "2":
            insertar_cursos()
        elif opcion == "3":
            inscripcion()
        elif opcion == "4":
            listar_usuarios()
        elif opcion == "5":
            listar_cursos()
        elif opcion == "6":
            listar_inscripciones()
        elif opcion == "0":
            cerrar_conexion()
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu()