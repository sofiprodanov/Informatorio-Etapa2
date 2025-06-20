Algoritmo ordenar_numeros
	
	Definir v1, v2, v3, aux Como Entero
	
	Escribir "Para poder ordenar decrecientemente los numeros, necesito que me indiques tres valores: "
	Leer v1, v2, v3
	
	Si v1 > v2 y v2 > v3 Entonces // si v1 es mayor que v2 y v2 es mayor a v3
		v1 = v1
	SiNo
		Si v2 > v1 Y v1 > v3 Entonces // si v2 es mayor, v1 el del medio y v3 el mas chico
			// aux toma el valor v1, v1 toma el valor de v2 y v2 toma el valor de aux, convirtiendo a v2 en el mayor y v1 en el del medio
			aux = v1
			v1 = v2
			v2 = aux
		SiNo
			Si v3 > v2 Y v2 > v1 Entonces // si v3 es mayor, v2 el del medio y v1 el mas chico
				// aux toma el valor v1, v1 toma el valor de v3 y v3 toma el valor del aux, convirtiendo a v3 en el mayor y v1 en el mas chico
				aux = v1
				v1 = v3
				v3 = aux
			SiNo
				Si v2 > v3 y v3 > v1 Entonces // si v2 es mayor, v3 el del medio y v1 el mas chico
					// aux toma el valor v1, v1 toma el valor de v2, v2 toma el valor de v3 y v3 toma el valor de aux,
					// convirtiendo a v2 el mayor, v3 el del medio y v1 el mas chico
					aux = v1
					v1 = v2
					v2 = v3
					v3 = aux
				FinSi
			FinSi
		FinSi
	FinSi
	
	Escribir v1,", " v2,", " v3,"."
	
FinAlgoritmo
