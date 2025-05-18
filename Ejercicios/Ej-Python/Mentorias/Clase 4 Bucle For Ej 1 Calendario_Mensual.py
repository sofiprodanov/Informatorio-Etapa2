#Ej 1: Mostrar los dias de un mes en formato lista. Dias fijos del 1 al 31.

import time

print("Calendario: ")

for dia in range (1, 32): #va 32 porque cuenta desde el nro 0
    print(f"- Dia {dia}")
    time.sleep(1)