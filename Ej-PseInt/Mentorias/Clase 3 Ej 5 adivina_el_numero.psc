Algoritmo adivina_el_numero
	
	Definir numsecreto, numelegido, intentos Como Entero
	numsecreto = 11
	intentos = 10
	
	Escribir "Hola! Este juego se llama Adivina el numero, en el cual debes elegir un numero del 1 al 100 y tienes 10 intentos."	
	
	Mientras intentos > 0 y numelegido <> numsecreto Hacer
		Repetir // para numeros fuera de rango
			Escribir "¿Que numero elegis?"
			Leer numelegido
			Si numelegido < 0 o numelegido > 100 Entonces
				Escribir "Numero fuera de rango. Ingresa un numero del 1 al 100."
			FinSi
		Hasta Que numelegido <= 100 y numelegido > 0
		
		intentos = intentos - 1
		
		Si numelegido < numsecreto y intentos > 0 Entonces // cuando nro es mayor o menor al nro secreto
				Escribir "El numero secreto es mayor. Intentalo de nuevo! Te quedan ", intentos," intentos. Elige otro numero: "
			SiNo
				Si numelegido > numsecreto y intentos > 0 Entonces
					Escribir "El numero secreto es menor. Intentalo de nuevo! Te quedan ", intentos," intentos. Elige otro numero: "
				FinSi
		FinSi
	FinMientras
	
	Si numelegido = numsecreto Entonces
		Escribir "Has ganado, adivinaste el numero secreto en el intento ", intentos,"!"
	SiNo
		Escribir "Has perdido! El numero secreto es ", numsecreto,"."
	FinSi
	
FinAlgoritmo
