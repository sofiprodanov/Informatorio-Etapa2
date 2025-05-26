# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Ingrese una palabra: ").lower()
vocales = ["a", "e", "i", "o", "u"]

# q = 0 asegura que el contador empiece desde cero cada vez que se cambia de vocal, permitiendo un conteo preciso para cada una.

for vocal in vocales:
    cantidad = 0 # Se reinicia para cada vocal, si estuviera fuera del bucle no se reiniciaria
    for letra in palabra:
        if letra == vocal:
            cantidad += 1
    print(f"La vocal {vocal} aparece {cantidad} veces.")