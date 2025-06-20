#ESTRUCTURAS DE CONTROL DE FLUJO: FOR - WHILE LOOPS
#WHILE
i = 1
while i <= 5:
    print(i)
    i += 1

#VARIABLES ESPECIALES
#CONTADOR > variable i: se utiliza para controlar por el incremento de su valor, la cantidad de iteraciones que vamos a realizar.
lista = [1, 2, 3, 4, 5]
pares = 0
i = 0

while i < len(lista):
    if lista[i] % 2 == 0:
        pares += 1
    i += 1

print(f"La cantidad de numeros pares hallados en la lista es de: {pares}")


#ACUMULADOR > cuando queremos almacenar/acumular los valores de una lista, tupla, diccionario u otro iterable
lista = [1, 2, 3, 4, 5]
suma = 0
i = 0

while i < len(lista):
    suma += lista[i]
    i += 1

print(f"El acumulador tiene la suma de: {suma}")



#BANDERA > Usamos valores booleanos para marcar si se cumplio una condicion.
lista = [1, 2, 3, 4, 5]
nro_buscado = 3
encontrado = False
i = 0

while i < len(lista):
    if lista[i] == nro_buscado:
        encontrado = True
        break
    i += 1

if encontrado:
    print("El numero se encuentra en la lista.")
else:
    print("El numero no se encuentra en la lista")



#BUCLE WHILE
usuario = input("Ingresa el usuario: ")
contrasenia = input("Ingresa la contraseña: ")

while usuario != "Informatorio" and contrasenia != "Info2023":
    print("El usuario o contraseña ingresado es incorrecto. Intenta nuevamente.")
    usuario = input("Ingresa el usuario: ")
    contrasenia = input("Ingresa la contraseña: ")
else:
    print("Ingresaste correctamente. Bienvenido.")



#POWERPOINT
contador = 1
while contador <= 5:
    print(contador)
    contador += 1


#USO DE BREAK Y CONTINUE
contador = 1
while contador <= 5:
    if contador == 3:
        break
    print(contador)
    contador += 1

contador = 1
while contador <= 5:
    contador += 1
    if contador == 3:
        continue
    print(contador)

#Bucle infinito
while True:
    respuesta = input("¿Quieres salir? 'si/no' ")
    if respuesta == "si":
        break


#programa que pide al usuario un numero y calcula la suma de todos los numeros
num = int(input("Ingresa un numero: "))
i = 1
suma = 0

while i <= num:
    suma += i
    i += 1
print("La suma de los numeros naturales del 1 hasta", num, "es:", sum)

#programa que pode al usuario un nro e imprime la tabla de mutiplicar correspondiente a ese numero del 1 al 10
num = int(input("Ingresa un numero: "))
i = 1

while i <= 10:
    print(num, "x", i, "-", num*1)
    i += 1

#programa que pide al usuario una palabra e imprime la misma palabra pero con letras en orden inverso
palabra = input("Ingresa una palabra: ")
palabra_invertida = ""

i = len(palabra) - 1

while i >= 0:
    palabra_invertida += palabra[i]
    i -= 1
print("La palabra invertida es: ", palabra_invertida)