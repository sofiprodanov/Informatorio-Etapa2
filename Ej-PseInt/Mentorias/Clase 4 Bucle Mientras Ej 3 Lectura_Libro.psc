Algoritmo Lectura_Libro
	
	//Ej 3: lee hasta llegar a la ultima pag del libro
	
	Definir pagina_actual, paginas_total Como Entero
	pagina_actual = 1
	
	Escribir "Total de paginas del libro: "
	Leer paginas_total
	
	Mientras pagina_actual <= paginas_total Hacer
		Escribir "Leyendo pagina ", pagina_actual "."
		pagina_actual = pagina_actual + 1 
		Esperar 5 Segundos
		
	FinMientras
	
	Escribir "Termine el libro."
	
	
	
	
FinAlgoritmo
