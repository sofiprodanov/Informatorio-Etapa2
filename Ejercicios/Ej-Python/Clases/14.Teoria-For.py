#ESTRUCTURAS DE CONTROL DE FLUJO: FOR - WHILE LOOPS
#FOR
secuencia = ""
for variable in secuencia:
    #Bloque de codigo a ejecutar en cada iteracion

#ITERANDO SOBRE UNA LISTA:
    numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)


#ITERANDO SOBRE UNA CADENA DE TEXTO
texto = "Hola mundo"

for letra in texto:
    print(letra)


#ITERANDO SOBRE UN DICCIONARIO
estudiantes = {
    "Juan": 18,
    "Maria": 20,
    "Pedro": 19
}

for estudiantes in estudiantes:
    print(estudiantes)


#ITERANDO SOBRE UN RANGO DE VALORES
for i in range(1, 6):
    print(i)


#CONTROL DE BUCLES: BREAK Y CONTINUE (P/WHILE Y FOR)
#BREAK > detener la ejecucion del ciclo en el punto en el que se encuentra.
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero == 3:
        break
    print(numero)

#CONTINUE > saltar la iteracion actual del ciclo y pasar al siguiente.
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero == 3:
        continue
    print(numero)


#POWER POINT
#Iterar sobre una lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

secuencia = [1, 2, 3, 4, 5]
for elemento in secuencia:
    #bloque de codigo

#Existen dos herramientas que van a ser de gran utilizadad para generar secuencias
# range(): Se utiliza para generar una secuencia de números, que se pueden usar para iterar en un bucle for. Es especialmente útil cuando necesitás un número 
#conocido de iteraciones.
#Sintaxis de range()
   # range() : Puede tomar hasta tres argumentos:
   # range(stop) : Genera números desde 0 hasta stop - 1.
   # range(start, stop): Genera números desde start hasta stop - 1.
   # range(start, stop, step) : Genera números desde start hasta stop - 1, incrementando por step (este último es opcional, por defecto es 1).
# enumerate(): Añade un contador a un iterable y lo devuelve en forma de un objeto enumerado. Esto es útil cuando necesitás tanto el índice como el valor
#del elemento en un bucle for.
# Sintaxis de enumerate()
    # enumerate(iterable, start=0)
    # iterable: La secuencia que querés enumerar (por ejemplo, una lista).
    # start: El valor inicial del contador (opcional, por defecto es 0)



    palabra = "Python"
    for letra in palabra:
        print(letra)


for i in range(5):
    print(i)

#ITERAR SOBRE UN DICCIONARIO
#Iterar sobre las claves
diccionario = {"a": 1, "b": 2, "c": 3}
for clave in diccionario:
    print(clave)
print("---")

#Iterar sobre los valores
for valor in diccionario.values():
    print(valor)
print("---")

#Iterar sobre claves y valores:
for clave, valor in diccionario.items():
    print(clave, valor)