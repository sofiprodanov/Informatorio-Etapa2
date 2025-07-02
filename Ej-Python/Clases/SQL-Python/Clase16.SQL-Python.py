import sqlite3
import uuid
import datetime

conn = sqlite3.connect('blog.db') #nombre de la base de datos, si no la encuentra la crea.

cursor = conn.cursor() #ejecutar para crear tablas

def crear_tabla():
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        uuid VARCHAR PRIMARY KEY,
        username VARCHAR UNIQUE NOT NULL,
        email VARCHAR UNIQUE NOT NULL,
        password VARCHAR NOT NULL,
        created_at TIMESTAMP NOT NULL
        )
    ''')

    #categoria
    #posts
    #comentarios

def insertar_usuario():
    username = input('Inserte el nombre de usuario: ').strip() #strip avisa si hay espacios
    email = input('Inserte el email de usuario: ').strip()
    password = input('Inserte el password de usuario: ')
    #validaciones(que cumpla ciertos caracteres o cantidad de caracteres)


    
    #proceso (+ encriptar password) - opcional
    user_uuid = uuid.uuid4()
    created_at = datetime.datetime.now() #se pone dos veces porque en el primero se llama al modulo y luego importar
    
    query = f'''INSERT INTO usuarios(uuid, username, email, password, created_at) 
        VALUES (?, ?, ?, ?, ?)
        ''' #PARA INSERTAR DATOS
    #INVESTIGAR COMO SUCEDE UNA INYECCION SQL

    cursor.execute(query, (str(user_uuid), username, email, password, created_at)) #username si se hacen validaciones deberia ir como valid_username por ej
    conn.commit()
    #poner un try except
    print("Usuario registrado correctamente.")
        
    
    #populo a la db (insertar en base de datos)
    pass

def insertar_post():
    pass

def insertar_categoria():
    pass

def listar_usuario():
    pass

def listar_categoria():
    pass

def salir():
    pass


def menu(): 
    crear_tabla() #se crea la tabla antes del while ya que sino cada vez va a crear la tabla
    while True:
        print('\nMenu')
        print("1. Insertar un usuario")
        print("2. Crear un post")
        print("3. Insertar una categoria")
        print("4. Listar usuario")
        print("5. Listar categoria")
        print("0. Salir")
        
        opcion = input("Seleccione una opcion: ")

        if (opcion == "1"):
            insertar_usuario()
        elif (opcion == "2"):
            insertar_post()
        elif (opcion == "3"):
            insertar_categoria()
        elif (opcion == "4"):
            listar_usuario()
        elif (opcion == "5"):
            listar_categoria()
        elif (opcion == "0"):
            break
        else:
            print('Opcion no valida, intente nuevamente.')

menu()