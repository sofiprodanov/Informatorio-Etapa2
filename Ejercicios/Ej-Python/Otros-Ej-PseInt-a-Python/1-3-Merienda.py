#3. Elabore un algoritmo para representar la acción de servir la merienda. El comensal puede tomar té, café, café con leche, té con leche
# y puede o no ponerle azúcar, si le pone puede ponerle una, dos o tres cucharadas.

print("Hora de la merienda! Que te gustaria tomar? Las opciones son:")

while True: #cuando el cliente ingresa un numero de opcion fuera del rango indicado
    print("1. Té")
    print("2. Café")
    print("3. Café c/leche") 
    print("4. Té c/leche")
    op = int(input("Indica el numero de opcion: "))
    
    if op == 1:
        bebida = "Té"
        break
    elif op == 2:
        bebida = "Café"
        break
    elif op == 3:
        bebida = "Café c/leche"
        break
    elif op == 4:
        bebida = "Té c/leche"
        break
    else:
        print("La opción que me indicas no se encuentra disponible dentro de la carta. Las opciones disponibles son (indicar con el número): ")

while True: #cliente pide cantidad de cucharadas distintas a las indicadas
    print("¿Cuántas cucharadas de azúcar te gustaría? Ninguna (cero), 1, 2 o 3 cucharadas?")
    azucar = int(input())
    
    if azucar < 0 or azucar > 3:
        print("La cantidad está fuera del rango indicado.")
    else:
        break

if azucar == 0: #confirma la orden con la cantidad de azucar
    print(f"Perfecto! Entonces su orden es {bebida} sin azúcar.")
else:
    print(f"Perfecto! Entonces su orden es {bebida} con {azucar} cucharadas de azúcar.")
