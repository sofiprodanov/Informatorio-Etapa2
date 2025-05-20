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