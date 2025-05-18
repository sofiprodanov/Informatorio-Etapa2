#Ej 2: Monitoreo de la bateria hasta que necesite recarga.

import time

#Validamos que el nivel de bateria este entre 0 y 100
while True:
    nivel_bateria = int(input("Indica cual es el nivel de bateria: "))
    if 0 <= nivel_bateria <= 100:
        break #si es valido, salimos del bucle
    else:
        print("¡Valor invalido! Ingresa un numero entre 0 y 100.")

#Monitoreo de la bateria
while nivel_bateria > 0:
    if nivel_bateria > 20:
        print("Todavia tienes bateria.")
    elif nivel_bateria > 5:
        print("¡Bateria baja! Conecte el cargador.")
    elif nivel_bateria <= 5:
        print("¡Bateria critica! Conecte el cargador inmediatamente.")
    
    nivel_bateria -= 5 #Restamos 5% en cada iteracion
    if nivel_bateria <0: #Evitamos valores negativos
        nivel_bateria = 0

    print(f"Te queda {nivel_bateria}% de bateria.")
    time.sleep(5) #espera de 5 segundos entre verificaciones

print("Bateria critica. Apagando...")
