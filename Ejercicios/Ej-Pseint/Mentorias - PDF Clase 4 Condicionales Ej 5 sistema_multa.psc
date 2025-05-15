Algoritmo sistema_multa
	
	//Ej 5: Sistema de multas por exceso de velocidad en zonas urbanas
	
	Definir vias Como Caracter
	Definir velocidad Como Entero
	
	Escribir "¿Vas por calle o avenida?"
	Leer vias
	
	Escribir "¿A que velocidad vas? (solo numeros)"
	Leer velocidad
	
	max_calle = 40
	max_av = 60
	
	Si vias = "calle" Entonces
		Si velocidad <= max_calle Entonces
			Imprimir "Cumple con las normas."
		SiNo
			Si velocidad > max_calle Entonces
				Imprimir "Tiene una multa por exceso de velocidad."
			FinSi
		FinSi
	SiNo
		Si vias = "avenida" Entonces
			Si	velocidad <= max_av Entonces
				Imprimir "Cumple con las normas."
			SiNo
				Si velocidad > max_av Entonces
					Imprimir "Tiene una multa por exceso de velocidad."
				FinSi
			FinSi
		FinSi
	FinSi
		
FinAlgoritmo
