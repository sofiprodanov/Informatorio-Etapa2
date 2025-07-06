#Ej 2: Simulacion de un semaforo

#.lower() hace que python no distinga las minusculas de las mayusculas

luz = input("Ingrese el color del semaforo: \n").lower()

if luz == "verde":
    print("Avanza! Gracias por la paciencia")
elif luz == "amarillo":
    print("Precaucion! Reduce la velocidad por favor.")
elif luz == "rojo":
    print("Detente! Por favor.")
else:
    print("Introduzca un color de semaforo valido.")