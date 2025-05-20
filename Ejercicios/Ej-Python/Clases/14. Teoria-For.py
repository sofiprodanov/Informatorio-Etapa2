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