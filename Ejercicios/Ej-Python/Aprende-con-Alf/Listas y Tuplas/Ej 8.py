#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


palabra = input("Ingresa una palabra: ")
if palabra == palabra[::-1]: #palabra[::-1] es un slicing que crea una versión invertida de la cadena original.
    print("Es un palindromo.")
else:
    print("No es un palindromo.")



