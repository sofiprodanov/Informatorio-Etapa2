# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Ingrese una palabra: ").lower()
vocales = ["a", "e", "i", "o", "u"]

palabra = list(palabra)
letraA = palabra.count("a")
letraE = palabra.count("e")
letraI = palabra.count("i")
letraO = palabra.count("o")
letraU = palabra.count("u")

print(f"La vocal 'a' aparece {letraA} veces.")
print(f"La vocal 'e' aparece {letraE} veces.")
print(f"La vocal 'i' aparece {letraI} veces.")
print(f"La vocal 'o' aparece {letraO} veces.")
print(f"La vocal 'u' aparece {letraU} veces.")
