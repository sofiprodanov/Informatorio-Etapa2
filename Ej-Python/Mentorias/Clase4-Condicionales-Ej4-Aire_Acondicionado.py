#Ej 4: Control de temperatura del aire acondicionado.

try:
    temperatura = int(input("¿Cuantos grados hace actualmente? \n"))

    if temperatura >= 26:
        print("Recomendacion: Deberias encender el aire acondicionado.")
    elif temperatura <= 13:
        print("Recomendacion: Deberias encender la calefaccion.")
    else:
        print("La temperatura es agradable! No necesitas climatizacion.")
except ValueError:
    print("Error: Por favor ingresa un numero valido de grados.")