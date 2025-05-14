Algoritmo tabla_multiplicacion
	
	Definir number, resultado, i Como entero
	
	Escribir "Escribe un numero del 1 al 10: "
	Leer number
	
	// con paso 1 ---> porque va a ir de uno en uno (+1), desde 1
	// con paso 2 --> va a sumar 2 en 2, ej:1, 3, 5, 7, etc.
	Para i = 1 Hasta 10 Con Paso 1 Hacer
		resultado = number * i 
		Escribir number, " x ", i, " = ", resultado
	Fin Para
	
	//si escribimos por fuera "Escribir resultado" va a poner solo el rdo final
FinAlgoritmo
