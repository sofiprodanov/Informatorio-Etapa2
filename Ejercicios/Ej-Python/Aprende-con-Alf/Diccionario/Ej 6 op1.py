#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre,
#edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe
#imprimirse el contenido del diccionario.

persona = {}

while True:
    preg_nombre = input("Cual es tu nombre? ")
    persona["nombre"] = preg_nombre
    preg_edad = input("Cual es tu edad? ")
    persona["edad"] = preg_edad
    preg_sexo = input("Cual es tu genero? ")
    persona["sexo"] = preg_sexo
    preg_tel = input("Cual es tu telefono? ")
    persona["tel"] = preg_tel
    preg_email = input("Cual es tu correo electronico? ")
    persona["email"] = preg_email

    respuesta = print("Desea agregar una nueva persona? s/n")
    if respuesta == "n":
        break

for informacion, datos in persona.items():
    print(informacion, datos)

