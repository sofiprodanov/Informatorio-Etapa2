# Guarda las respuestas de varias personas (3) en un diccionario con nombre como clave y una 
#lista de sus respuestas como valor

encuesta = {}

for i in range(3):
    nombre = input("Nombre: ")
    respuesta = input("Te gusto el producto? ")
    encuesta[nombre] = [respuesta]

print(encuesta)