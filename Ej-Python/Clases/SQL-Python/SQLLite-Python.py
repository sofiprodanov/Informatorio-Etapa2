import sqlite3
import uuid
import datetime

conn = sqlite3.connect('blog.db') #nombre de la base de datos, si no la encuentra la crea.

cursor = conn.cursor() #ejecutar para crear tablas

#aplica la restricción de integridad referencial (En resumen, evita que por ejemplo: se agregue un usuarios_uuid a posts si ese UUID no existe en usuarios)
cursor.execute("PRAGMA foreign_keys = ON") 

def crear_tabla():
    #usuarios
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
        uuid_username VARCHAR PRIMARY KEY,
        username VARCHAR UNIQUE NOT NULL,
        email VARCHAR UNIQUE NOT NULL,
        password VARCHAR NOT NULL,
        created_at TIMESTAMP NOT NULL
        )
    ''')

    #categorias
    cursor.execute('''CREATE TABLE IF NOT EXISTS categorias(
        uuid_category VARCHAR PRIMARY KEY,
        name VARCHAR UNIQUE NOT NULL
        )
    ''')
    
    #posts
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts(
        uuid_post VARCHAR PRIMARY KEY,
        title VARCHAR NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL,
        uuid_username VARCHAR,
        FOREIGN KEY (uuid_username) REFERENCES usuarios(uuid_username)
        )
    ''')
    
    #post_categorias
    cursor.execute('''CREATE TABLE IF NOT EXISTS posts_categorias(
        uuid_post VARCHAR,
        uuid_category VARCHAR,
        FOREIGN KEY (uuid_post) REFERENCES posts(uuid_post),
        FOREIGN KEY (uuid_category) REFERENCES categorias(uuid_category)
    )
    ''')
    
    # comentarios
    cursor.execute('''CREATE TABLE IF NOT EXISTS comentarios(
        uuid_comment VARCHAR PRIMARY KEY,
        content TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL,
        uuid_username VARCHAR,
        uuid_post VARCHAR,
        FOREIGN KEY (uuid_username) REFERENCES usuarios(uuid_username),
        FOREIGN KEY (uuid_post) REFERENCES posts(uuid_post)
    )
    ''')

    conn.commit()

def insertar_usuario():
    try:
        uuid_username = str(uuid.uuid4()) # --- Genera UUID ---
        username = input('Inserte el nombre de usuario: ').strip() #strip avisa si hay espacios
        email = input('Inserte el email de usuario: ').strip()
        password = input('Inserte la contraseña de usuario: ').strip()
        created_at = datetime.datetime.now() # --- Generar fecha --- // se pone dos veces porque en el primero se llama al modulo y luego importar

        # --- Validaciones ---
        if not username:
            raise ValueError("El nombre de usuario no puede estar vacío.")
        if len(username) < 3:
            raise ValueError("El nombre de usuario debe tener al menos 3 caracteres.")
        if '@' not in email or '.' not in email:
            raise ValueError("El email ingresado no es válido.")
        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")

        #proceso (+ encriptar password) - opcional
    
        # --- Insertar en base de datos ---
        query = '''INSERT INTO usuarios(uuid_username, username, email, password, created_at) 
                VALUES (?, ?, ?, ?, ?)
            ''' #PARA INSERTAR DATOS PARA EVITAR UNA INYECCION SQL

        cursor.execute(query, (uuid_username, username, email, password, created_at))
        conn.commit()
        print("Usuario registrado correctamente.")

    except ValueError as ve:
        print(f"Error de validación: {ve}")

    except sqlite3.Error as db_err:
        print(f"Error de base de datos: {db_err}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


def insertar_post():
    try:
        uuid_post = str(uuid.uuid4())

        listar_usuario()
        uuid_username = input("UUID del usuario que va a postear: ").strip()
        if not uuid_username:
            raise ValueError("Debe ingresar un UUID de usuario válido.")

        listar_categoria()
        uuid_category = input("UUID de la categoría del post: ").strip()
        if not uuid_category:
            raise ValueError("Debe ingresar un UUID de categoría válido.")

        title = input("Ingrese el título de su post: ").strip()
        if not title:
            raise ValueError("El título no puede estar vacío.")
        if len(title) < 5:
            raise ValueError("El título debe tener al menos 5 caracteres.")

        content = input("Introduzca una descripción del post: ").strip()
        if not content:
            raise ValueError("La descripción no puede estar vacía.")
        if len(content) < 10:
            raise ValueError("La descripción debe tener al menos 10 caracteres.")

        created_at = datetime.datetime.now()

        query_post = '''INSERT INTO posts (uuid_post, title, content, created_at, uuid_username)
                    VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(query_post, (uuid_post, title, content, created_at, uuid_username))
        conn.commit()

        query_categoria = '''INSERT INTO posts_categorias (uuid_post, uuid_category)
                        VALUES (?, ?)'''
        cursor.execute(query_categoria, (uuid_post, uuid_category))
        conn.commit()

        print("Post cargado correctamente.")

    except ValueError as ve:
        print(f"Error de validación: {ve}")

    except sqlite3.Error as db_err:
        print(f"Error de base de datos: {db_err}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def insertar_comentario():
    try:
        listar_usuario()
        uuid_username = input("UUID del usuario que comenta: ").strip()

        cursor.execute("SELECT 1 FROM usuarios WHERE uuid = ?", (uuid_username,)) #verifica si existe el usuario
        if not cursor.fetchone(): #verifica si el uuid de post existe en la tabla post, si no se encuentra detiene la funcion
            print("El UUID de usuario no existe.")
            return

        listar_post()
        uuid_post = input("UUID del post que se quiere comentar: ").strip()

        cursor.execute("SELECT 1 FROM posts WHERE uuid = ?", (uuid_post,)) #verifica si existe el post
        if not cursor.fetchone():
            print("El UUID del post no existe.")
            return

        content = input("Ingrese el comentario: ").strip()
        if not content:
            print("El comentario no puede estar vacío.")
            return

        uuid_comment = str(uuid.uuid4())
        created_at = datetime.datetime.now()

        query = '''INSERT INTO comentarios (uuid_comment, content, created_at, uuid_username, uuid_post)
                VALUES (?, ?, ?, ?, ?)'''

        cursor.execute(query, (uuid_comment, content, created_at, uuid_username, uuid_post))
        conn.commit()

        print("Comentario agregado correctamente.")
    except sqlite3.IntegrityError as e: #Captura errores de integridad de la base de datos (como claves foráneas inválidas).
        print("Error de integridad:", e) #Muestra el error exacto.
    except Exception as e: #Captura cualquier otro error inesperado.
        print("Error inesperado:", e) #Muestra el detalle del error general.

def insertar_categoria():
    category_name = input("Inserte la categoría: ").strip()
    uuid_category = str(uuid.uuid4())

    query = '''INSERT INTO categorias (uuid_category, name)
        VALUES (?, ?)'''

    cursor.execute(query, (uuid_category, category_name))
    conn.commit()
    print(f"Categoría {category_name} creada exitosamente.")

def listar_usuario():
    cursor.execute("SELECT uuid_username, username FROM usuarios")
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(u)

def listar_post():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    for p in posts:
        print(p)

def listar_categoria():
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    for c in categorias:
        print(c)

def salir():
    cursor.close()
    conn.close()

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