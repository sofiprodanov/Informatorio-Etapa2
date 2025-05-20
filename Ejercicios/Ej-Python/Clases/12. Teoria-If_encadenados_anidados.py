#ESTRUCTURAS DE CONTROL - CONDICIONALES

#IF ENCADENADOS
edad = 15
if edad >= 16:
    print("Usted puede votar.")
if edad < 16:
    print("Usted NO puede votar.")

#IF ENCADENADOS
edad1 = 16
edad2 = 21
if edad1 >= 16:
    print("Usted puede votar.")
    if edad2 >= 21:
        print("Usted puede viajar fuera del pais.")

#casos con + de una comparacion, o + de una condicion para que se realice la accion
usuario = "Informatorio"
contrasenia = "Info2023"

if usuario == "Informatorio" and contrasenia == "Info2023":
    print("Acceso correcto. Bienvenido")

#OPERADORES LOGICOS > AND, OR, NOT

#IF, ELSE, ELIF
#El programa verifica el primer condicional y como retorna un valor True no se ejecuta el resto de los bloques de codigo.
nota1 = 1
nota2 = 2
nota3 = 3
promedio_notas = (nota1 + nota2 + nota3)/3

if promedio_notas < 6:
    print(f"Por lo visto no estas leyendo los apuntes ni practicando. Desaprobaste. Tu promedio es: {promedio_notas}.")
elif promedio_notas < 8:
    print(f"¡Aprobaste!¡Pero con mas practica vas a lograr mas! Tu promedio es: {promedio_notas}.")
else:
    print(f"¡Excelente! Se nota que estas leyendo los apuntes y practicando. Tu promedio es: {promedio_notas}.")


#El programa verifica el primer condicional y como retorna un valor False, pasa a la siguiente condcondicion y esta retorna un valor True, y ejecuta ese 
# bloque de codigo
nota1 = 5
nota2 = 7
nota3 = 9
promedio_notas = (nota1 + nota2 + nota3)/3

if promedio_notas < 6:
    print(f"Por lo visto no estas leyendo los apuntes ni practicando. Desaprobaste. Tu promedio es: {promedio_notas}.")
elif promedio_notas < 8:
    print(f"¡Aprobaste!¡Pero con mas practica vas a lograr mas! Tu promedio es: {promedio_notas}.")
else:
    print(f"¡Excelente! Se nota que estas leyendo los apuntes y practicando. Tu promedio es: {promedio_notas}.")


#El programa verifica el primer condicional y como retorna un valor False, pasa a la siguiente condicion y esta tambien retorna un valor False, entonces
# pasa a la siguiente condicion y como devuelve un valor True, y ejecuta ese bloque de codigo
nota1 = 10
nota2 = 10
nota3 = 10
promedio_notas = (nota1 + nota2 + nota3)/3

if promedio_notas < 6:
    print(f"Por lo visto no estas leyendo los apuntes ni practicando. Desaprobaste. Tu promedio es: {promedio_notas}.")
elif promedio_notas < 8:
    print(f"¡Aprobaste!¡Pero con mas practica vas a lograr mas! Tu promedio es: {promedio_notas}.")
else:
    print(f"¡Excelente! Se nota que estas leyendo los apuntes y practicando. Tu promedio es: {promedio_notas}.")


#POWERPOINT
color_1 = "Blanco"
color_2 = "Negro"
color_3 = "Blanco"

if color_1 == color_2:
    print("Los colores 1 y 2 son iguales.")
elif color_1 == color_3:
    print("Los colores 1 y 3 son iguales.")
else:
    print("Los colores 2 y 3 son iguales.")


#OPERADORES EN PYTHON:
#Operadores Logicos: AND(Y Logico), OR(O logico), NOT(Negacion Logica)
#Operadores de Comparacion: ==, !=, >, <, >=, <=, 

color_1 = "Blanco"
color_2 = "Negro"
color_3 = "Negro"

if color_1 != color_2 and color_2 != color_3:
    print("Los colores 1 y 3 son iguales.")
elif color_1 == color_2:
    print("Los colores 1 y 2 son iguales.")
else:
    print("Los colores 2 y 3 son iguales.")


#otroej
color_1 = "Blanco"
color_2 = "Negro"
color_3 = "Negro"

if color_1 != color_2: #solo un if
    if color_2 != color_3: #if anidado
        print("Los colores 1 y 3 son iguales.") #multiples condiciones"
    else:
        print("Los colores 2 y 3 son iguales.") #condicional alternativo o doble.
else:
    print("Los colores 1 y 2 son iguales.")


#creamos un programa que utiliza la funcion "input()"
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#agregamos uso de elif a nuestra estructura condicional
num = int(input("Ingresa un numero entero: "))
if num > 0:
    print(num, "es un numero positivo.")
elif num < 0:
    print(num, "es un numero negativo.")
else:
    print("El numero es cero.")

#mostrar las multiples condiciones
num = int(input("Ingresa un numero entero: "))
if num % 2 == 0 and num % 3 == 0:
    print(num, "es multiplo de 2 y de 3 a la vez.")
else:
    print(num, "no es multiplo de 2 y de 3 a la vez.")


#evaluamos el caracter ingresado por el usuario y como respuesta, decirle al usuario que tipo de caracter es, por eso utilizamos multiples condiciones.
caracter = input("Ingresa un caracter: ")
if caracter.isupper():
    print("El caracter es una letra mayuscula.")
elif caracter.islower():
    print("El caracter es una letra minuscula.")
elif caracter.isdigit():
    print("El caracter es un numero.")
else:
    print("El caracter es una caracter especial.")