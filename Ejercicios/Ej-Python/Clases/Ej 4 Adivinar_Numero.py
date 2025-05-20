import random

#Generar un numero secreto entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    #Pedir al usuario que ingrese su adivinanza
    adivinanza = input("Introduce tu adivinanza: ")

    #Verificar si la entrada es un numero
    if not adivinanza.isdigit():
        print("Por favor, introduce un numero valido.")
        continue

    #Convertir la entrada a un numero entero
    adivinanza = int(adivinanza)
    intentos += 1

    #Verificar la adivinanza
    if adivinanza < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo")
    elif adivinanza > numero_secreto:
        print("Demasiado bajo. Intenta de nuevo")
    else:
        print(f"¡Felicitaciones! Adivinaste el numero en {intentos} intentos.")
        break

print("Gracias por jugar. ¡Hasta la proxima!")