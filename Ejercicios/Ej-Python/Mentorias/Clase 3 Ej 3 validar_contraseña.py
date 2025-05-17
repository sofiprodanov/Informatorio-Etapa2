#Consigna: 
#Crear un programa que pida al usuario una contraseña. Mientras la contraseña ingresada no sea "1234", debe seguir pidiéndola.
#Cuando el usuario ingrese la contraseña correcta, mostrar un mensaje de acceso concedido.

#\n hace salto de linea

contrasenia = input("Ingrese la contraseña:\n")

while contrasenia != "1234":
    contrasenia = input ("Contraseña incorrecta, vuelva a ingresarla: ")

print("Acceso concedido")