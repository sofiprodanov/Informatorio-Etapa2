#Ej 2: Cuenta las vocales en una palabra.

#len(palabra) calcula cuántos caracteres tiene la cadena almacenada en la variable palabra

palabra = input("Ingrese una palabra: ")
contador_vocales = 0

for i in range(len(palabra)):
    letra = palabra[i].lower()
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador_vocales += 1

print("La palabra tiene", contador_vocales, "vocales.")