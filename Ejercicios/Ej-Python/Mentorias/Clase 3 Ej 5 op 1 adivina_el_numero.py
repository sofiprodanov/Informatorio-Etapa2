#Consigna:
#El programa elige un número secreto entre 1 y 100 (vos lo podés asignar directamente). El usuario debe adivinar el número.
#Después de cada intento, el programa debe decir si el número ingresado es mayor o menor que el número secreto.
#El usuario tiene un máximo de 10 intentos. Si lo adivina antes, mostrar un mensaje de felicitaciones indicando en qué intento lo logró.
#Si no lo adivina en 10 intentos, mostrar un mensaje diciendo que perdió.


#usar break a los 10 intentos

import random

#numsecreto = random.randint(1, 100) #elige un nro aleatorio entre 1 y 100
numsecreto = 11

intentosmax = 10
intentos = 0


print(f"Hola! Este juego se llama Adivina el numero, en el cual debes ingresar un numero entre 1 y 100 y tienes {intentosmax} intentos.")

while intentos < intentosmax:
	#solicitar nro hasta que este en el rango correcto
	while True:
		numelegido = int(input("¿Que numero eliges? \n"))
		if 1 <= numelegido <= 100:
			break
		print("Numero fuera de rango. Ingresa un numero del 1 al 100.")
		
	intentos += 1

	if numelegido == numsecreto:
		print(f"Has ganado! Adivinaste el numero secreto en el intento {intentos}.")
		break
	elif numelegido < numsecreto: #cuando el nro es mayor/menor al nro secreto
		print(f"El numero secreto es mayor.")
	elif numelegido > numsecreto:
		print(f"El numero secreto es menor.")
	
	#Mostrar intentos restantes (excepto si fue el ultimo)
	if intentos < intentosmax:
		print(f"Te quedan {intentosmax - intentos} intentos.")

#Si no adivino, muestra mensaje de derrota.
if intentos == intentosmax and numelegido != numsecreto:
	print(f"Has perdido! El numero secreto es {numsecreto}!")

    
