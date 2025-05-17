Algoritmo Peaje
	
	//8. Escriba un algoritmo que determine el precio del peaje a abonar por el pasajero en función de los km que va a recorrer, sabiendo que hasta 
	//10 km el precio es $ 200, hasta 20 km, el precio es $ 300, hasta 40 km, el precio es $400 y hasta 80 km el precio es $500, si supera los 80 Km el costo es de $600.
	
	Definir km Como Entero
	
	Escribir "Ingrese cuantos kilometros va a recorrer: "
	Leer km
	
	Si km < 10 Entonces
		Escribir "El costo del peaje es $200."
	Sino
		Si km < 20 Entonces
			Escribir "El costo del peaje es $300."
		Sino
			Si km < 40 Entonces
				Escribir "El precio del peaje es $400."
			SiNo
				Si km < 80 Entonces
					Escribir "El precio del peaje es $500."
				SiNo
					Escribir "El precio del peaje es de $600."
				FinSi
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
