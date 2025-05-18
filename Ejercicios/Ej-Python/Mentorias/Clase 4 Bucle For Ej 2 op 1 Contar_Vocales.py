#Ej 2: Cuenta las vocales en una palabra.

palabra = input("Ingrese una palabra: ")
contador_vocales = 0

for letra in palabra.lower():
    if letra in "aeiou":
        contador_vocales += 1

print(f"La palabra tiene {contador_vocales} vocales.")