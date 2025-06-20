# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar
# por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

persona1 = {
    "nombre": "",
    "edad": "",
    "direccion": "",
    "telefono": "",
}

nombre = input("¿Cual es tu nombre? ")
edad = int(input("¿Cual es tu edad? "))
direccion = input("¿Cual es tu direccion? ")
telefono = int(input("¿Cual es tu numero de telefono? "))

persona1["nombre"] = nombre
persona1["edad"] = edad
persona1["direccion"] = direccion
persona1["telefono"] = telefono

print(f"{persona1["nombre"]} tiene {persona1["edad"]} años, vive en {persona1["direccion"]} y su numero de telefono es {persona1["telefono"]}.")