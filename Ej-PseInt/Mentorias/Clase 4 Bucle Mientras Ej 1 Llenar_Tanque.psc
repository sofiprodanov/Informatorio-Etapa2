Algoritmo Llenar_Tanque
	
	//Ej 1: bombear agua hasta alcanzar el nivel maximo
	
	Definir nivel_actual, nivel_maximo Como Entero
	
	nivel_actual = 0
	nivel_maximo = 100
	
	Escribir "El nivel de carga de agua en el tanque se encuentra al: "
	
	Mientras nivel_actual < nivel_maximo Hacer
		
		nivel_actual = nivel_actual + 10
		Esperar 2 Segundos
		Escribir nivel_actual,"%"
		
	FinMientras
	
	Escribir "Tanque lleno."
	
FinAlgoritmo
