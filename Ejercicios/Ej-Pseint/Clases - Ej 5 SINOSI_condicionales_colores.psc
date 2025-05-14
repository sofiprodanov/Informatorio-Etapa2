Algoritmo SINOSI_condicionales_colores
	
	Definir color1, color2 Como Caracter
	
	color1 = "Blanco"
	color2 = "Negro"
	color3 = "Blanco"
	
	Si color1 = color2 Entonces
		Imprimir "Los colores 1 y 2 son iguales." //primer bloque de codigo
		
	SiNo Si color1 = color3 Entonces
		Imprimir "Los colores 1 y 3 son iguales." //segundo bloque de codigo
			
		Sino
			Imprimir "Los colores 2 y 3 son iguales." //tercer bloque de codigo
			
		FinSi
	FinSi
	
	
FinAlgoritmo
