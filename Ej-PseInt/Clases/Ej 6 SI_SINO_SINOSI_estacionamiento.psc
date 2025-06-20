Algoritmo SI_SINO_SINOSI_estacionamiento
	
	Definir monto_ingresado, valor_estacionamiento Como Entero
	
	valor_estacionamiento = 1000
	
	Imprimir "Bienvenido al estacionamiento del Info. El valor del estacionamiento es de $1000."
	Imprimir "Por favor ingrese el monto que va a pagar (solo numeros): "
	Leer monto_ingresado
	
	Si monto_ingresado = valor_estacionamiento Entonces
		//primer bloque de codigo
		Imprimir "Muchas gracias. Ahora la barrera se levantara y usted puede ingresar."
	SiNo Si monto_ingresado >= valor_estacionamiento Entonces
			//segundo bloque de codigo
			vuelto <- monto_ingresado - valor_estacionamiento // operacion para dar vuelto
			Imprimir "Muchas gracias, puede pasar. Su vuelto es: ", vuelto
		SiNo
			//tercer bloque de codigo
			Imprimir "El monto ingresado es menor al requerido. La barrera no se levantara."
		FinSi
	FinSi
	
FinAlgoritmo
