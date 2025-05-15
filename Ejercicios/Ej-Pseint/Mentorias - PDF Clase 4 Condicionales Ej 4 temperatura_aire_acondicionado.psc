Algoritmo temperatura_aire_acondicionado
	
	//Ej 4: Control de temperatura del aire acondicionado
	
	Definir temperatura Como Entero
	
	Escribir "¿Cuantos grados esta haciendo? (solo numeros): "
	Leer temperatura
	
	Si temperatura >= 26 Entonces
		Imprimir "Deberias encender el aire acondicionado."
	SiNo
		Si temperatura <= 13 Entonces
			Imprimir "Deberias encender la calefaccion."
		SiNo
			Imprimir "La temperatura es ideal."
		FinSi
	Fin Si
	
FinAlgoritmo
