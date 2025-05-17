Algoritmo semaforo
	
	//Ej 2: Simulacion de un semaforo
	
	Definir luz Como Caracter
	
	Escribir "Ingrese el color del semaforo: "
	Leer luz
	
	Si luz = "verde" Entonces
		Imprimir ("Avanza! Gracias por la paciencia.")
		
	SiNo
		Si luz = "amarillo" Entonces
			Imprimir ("Precaucion! Reduce la velocidad por favor")
			
		SiNo
			Si luz = "rojo" Entonces
				Imprimir ("Detente! Por favor")
				
			SiNo
				Imprimir ("Introduzca un color de semaforo valido.")
				
			FinSi
		FinSi
	Fin Si
	
FinAlgoritmo
