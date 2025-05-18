#Ej 4: Estado de la conexion a internet

import time

print("Sistema de verificacion de conexion a Internet.")
intentos = 0
conectado = False

while not conectado:
    intentos += 1
    respuesta = input(f"Intento {intentos}. ¿Conexion verificada?(si/no): ").lower().strip()

    if respuesta == "si":
        conectado = True
        print("\n¡Conexion exitosa!")
        print(f"Establecida despues de {intentos} intento(s)")

    elif respuesta == "no":
        print("Conexion fallida. Reintentando en 5 segundos...")
        time.sleep(5)
    else:
        print("Error: Responda solo si o no")
        intentos -= 1

print("Proceso completado.")
