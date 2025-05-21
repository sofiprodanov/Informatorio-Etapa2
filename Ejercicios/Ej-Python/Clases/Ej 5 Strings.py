print("###STRINGS###")

nombre = "Pablo"
edad = 26

saludo = "Hola me llamo {nombre} y tengo {edad}".format(nombre, edad) #.format() es para formatear el texto
print(saludo)

a = 7
b = 20
mensaje = f"Hola me llamo {nombre} y tengo {a + b}"
print(mensaje)



print("### OPERACIONES CON STRING ###")

cadena1 = "Hola "
cadena2 = "Info"
cadena_concatenada = cadena1 + " " +cadena2
print(cadena_concatenada)

cadena_repetida = cadena2 *3
print(cadena_repetida)


cadena = "Hola mundo"
longitud = len(cadena)
print(longitud)


subcadena = cadena[0:4]
print(subcadena)

cadena_invertida = cadena[::-1] #con los :: pide que se invierta toda la cadena
print(cadena_invertida)


cadena_mayuscula = cadena.upper() #pasa a mayuscula
print(cadena_mayuscula)

cadena_minuscula = cadena_mayuscula.lower() #pasa a minuscula
print(cadena_minuscula)

cadena = cadena_minuscula.capitalize() #
print(cadena_minuscula)

cadena_reemplazo = cadena.replace("Hola", "algo") #reemplaza strings
print(cadena_reemplazo)

print("Hola\nMundo") #salto de linea
print("Hola\tMundo") #sangria o tabulacion
print("Hola\\Mundo")
print("Hola"'Mundo')
print("Hola \"Mundo\"") #pone comillas solo a mundo

print("Hola", end="!") #al final del primer string le pone el !, puede ir un salto de linea \n, etc.
print("Mundo")

print("Hola", "mundo", "info", sap="!") #hace espacios entre palabras




