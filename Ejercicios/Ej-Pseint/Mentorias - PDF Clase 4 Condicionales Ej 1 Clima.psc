Algoritmo clima
	
	//Ej 1: Decidir que ropa ponerse segun el clima
	Definir tiempo Como Caracter
	
	Escribir "Comentame como esta el tiempo y te ayudo a decidir que ponerte! Esta soleado, templado o lluvioso? "
	Leer tiempo
	
	Si tiempo = "soleado" Entonces
		Imprimir ("Usa ropa clara! No te olvides del protector solar y anteojos de sol.")
		
	Sino Si tiempo = "templado" Entonces
			Imprimir ("El clima esta templado, usa ropa normal. Disfruta el dia!")
			
		SiNo
			Si tiempo = "lluvioso" Entonces
				Imprimir ("No te olvides del paraguas y botas de lluvia!")
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
