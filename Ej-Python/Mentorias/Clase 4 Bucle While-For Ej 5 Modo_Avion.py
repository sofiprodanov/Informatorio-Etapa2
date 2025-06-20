#Ej 5: Reintentar conexion hasta que el modo avion este desactivado

import time

print("Sistema de verificacion de Modo Avion")

while True:
    respuesta = input("¿Se encuentra activo el modo avion?(si/no): ").lower().strip()

    #Validacion de respuesta
    if respuesta not in ('si', 'no'):
        print("\nERROR: Por favor ingrese unicamente 'si' o 'no'.")
        continue

    if respuesta == "si":
        print("\nALERTA: Modo avion ACTIVADO")
        print("Estado: SIN CONEXION A INTERNET")
        break
    
    else:
        print("Modo avion DESACTIVADO")
        print("Conectando a la red...")

    #Simulacion de conexion progresiva
    for i in range (5, 0, -1):
        print(f"Estableciendo conexion... {i} segundos restantes.")
        time.sleep(2)
    
    print("\n¡CONEXION EXITOSA!")
    print("Estado: CONECTADO A LA RED")
    break