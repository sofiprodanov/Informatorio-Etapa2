Algoritmo mayor_valor
	// 2. Elaborar un algoritmo para determinar el mayor de cuatro valores.
	
	Definir v1, v2, v3, v4, mayorvalor Como Real
	
	Escribir "Para indicar cual de los numeros es el mayor, necesito que me indiques cuatro valores: "
	Leer v1, v2, v3, v4 //los va a pedir como lo hace normalmente (en vertical)

	Si (v1 > v2) y (v1 > v3) y (v1 > v4) Entonces
		mayorvalor = v1 
	SiNo
		Si (v2 > v1) y (v2 > v3) y (v2 > v4) Entonces
			mayorvalor = v2
		SiNo
			Si (v3 > v1) y (v3 > v2) y (v3 > v4) Entonces
				mayorvalor = v3
			SiNo
				mayorvalor = v4
			FinSi
		FinSi
	Fin Si
	Escribir "El ", mayorvalor," es el mayor de los cuatro valores."
FinAlgoritmo
