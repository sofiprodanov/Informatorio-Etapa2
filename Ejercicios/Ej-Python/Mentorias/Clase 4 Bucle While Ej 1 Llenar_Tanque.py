#Ej 1: bombear agua hasta alcanzar el nivel maximo

import time

lvl_actual = 0
lvl_max = 100

print(f"El nivel de carga de agua en el tanque se encuentra al: ")
      
while lvl_actual < lvl_max:
    lvl_actual += 10
    time.sleep(2) #Esperar 2 segundos
    print(f"{lvl_actual}%")

print("Tanque lleno.")