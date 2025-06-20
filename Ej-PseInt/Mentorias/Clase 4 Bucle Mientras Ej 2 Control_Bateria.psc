Algoritmo ControlarBateria
	
	//Ej 2: Monitoreo de la bateria hasta que necesite recarga.
	
	Definir nivel_bateria Como Entero
	
	Escribir "Indica cual es el nivel de bateria: "
	Leer nivel_bateria
	
	Mientras nivel_bateria > 0 Hacer
		Si nivel_bateria > 20 y nivel_bateria < 100 Entonces //indica s/nivel de bateria
			Escribir "Todavia tienes bateria."
			
		SiNo
			Si nivel_bateria >= 5 y nivel_bateria <= 20 Entonces
				Escribir "¡Bateria baja! Conecte el cargador."
			FinSi
		FinSi
		
		Si	nivel_bateria <= 5 Entonces // verifica si al restar 5 llega a negativo
			nivel_bateria = 0
		SiNo
			nivel_bateria = nivel_bateria - 5 //simula consumo
		FinSi
		
		Esperar 5 Segundos //Espera entre verificaciones
		Escribir "Te queda " nivel_bateria "% de bateria."
		
	FinMientras
	
	Escribir "Bateria critica. Apagando..."
	
FinAlgoritmo
