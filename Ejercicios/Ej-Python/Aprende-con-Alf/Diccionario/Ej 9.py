# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la
# clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú:
# (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En 
# función de la opción elegida el programa tendrá que hacer lo siguiente:
# 1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# 2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 3. Preguntar por el NIF del cliente y mostrar sus datos.
# 4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# 6. Terminar el programa.

clientes = {}
opciones = " "

while opciones != "6":
    #VALIDACION DE NIF  
    while True:
        if nif in clientes:
            print("¡Error! Este NIF ya está registrado.")
        else:
            break
    #AGREGAR CLIENTE
    if opciones == "1":
        nif = input("Introduce NIF del cliente: ")
        nombre = input("Ingresa el nombre del cliente: ")
        direccion = input("Ingresa la direccion del cliente: ")
        tel = input("Ingresa el telefono del cliente: ")
        correo_electronico = input("Ingresa el correo electronico del cliente: ")
        vip = input("Es un cliente preferente?si/no: ").lower()
        cliente = {"nombre": nombre, 
                   "direccion": direccion, 
                   "tel": tel, 
                   "email": correo_electronico, 
                   "preferente": vip == "si"
                }
        clientes[nif] = cliente
    #ELIMINAR CLIENTE
    elif opciones == "2":
        nif = input("Introduce NIF del cliente: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print(f"No exite el cliente con el nif {nif}.")
    #MOSTRAR CLIENTE
    elif opciones == "3":
        nif = input("Introduce NIF del cliente: ")
        if nif in clientes:
            print(f"NIF: {nif}")
            for clave, valor in clientes[nif].items(): #recorre todos los campos del cliente/ clave = nif, valor = datos del cliente
                print(f"{clave.title()}: {valor}") #muestra cada campo y su valor
        else:
            print(f"No exite el cliente con el nif {nif}.")
    #LISTAR TODOS LOS CLIENTES
    elif opciones == "4":
        print("Lista de clientes: ")
        for clave, valor in clientes.items():
            print(clave, valor["nombre"]) #muestra la clave = nif + valor = nombre (uno de los datos del cliente)
    #LISTAR CLIENTES PREFERENTES
    elif opciones == "5":
        print("Lista de clientes preferentes: ")
        for clave, valor in clientes.items(): 
            if valor["preferente"]: #si tiene valor=preferente
                print(clave, valor["nombre"])
    elif opciones not in ["", " "]:
        print("Opcion no valida. Por favor elige una opcion del 1 al 6.")
    
    #OP 6 TERMINAR
    opciones = input("Menu de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción: ")


