#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre,
#edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe
#imprimirse el contenido del diccionario.

persona = {}

while True:
    clave = input("Que dato quieres ingresar? ") #Se pide al usuario que ingrese el nombre del dato que quiere guardar
    valor = input(clave + ": ") #Se pide el valor asociado a esa clave
    persona[clave] = valor
    print(persona)
    respuesta = input("Desea agregar una nuevo dato?si/no ").lower()
    if respuesta == "no":
        break

print(persona)

#  respuesta = input("Desea agregar una nuevo dato?si/no ").lower() == "si"