Algoritmo Modo_Avion
	
	//Ej 5: Reintentar conexión hasta que el modo avión esté desactivado.
	
	Definir respuesta Como Cadena
	Definir mod_avion, estadomodoavion Como Logico
	
	mod_avion = Falso
	estadomodoavion = Falso
	
    Mientras mod_avion = Falso Hacer
		Escribir "¿El modo avion se encuentra activo?"
		Leer respuesta
		Si respuesta = "si" Entonces
			estadomodoavion = Verdadero
		FinSi
		
		Si estadomodoavion = Verdadero Entonces
			mod_avion = Verdadero
			Escribir "El modo avion esta activado. No hay conexion."
		SiNo
			Escribir "Modo avion desactivado. Conectando a red..."
			Esperar 2 Segundos
		FinSi
    FinMientras

FinAlgoritmo
