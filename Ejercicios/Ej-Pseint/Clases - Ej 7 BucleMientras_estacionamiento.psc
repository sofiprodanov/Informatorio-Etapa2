Algoritmo Mientras_estacionamiento
	
	Definir monto_ingresado, valor_estacionamiento Como Entero
	
	valor_estacionamiento = 1000
	
	Imprimir "Bienvenido al estacionamiento del Info. El valor del estacionamiento es de $1000."
	Imprimir "Por favor ingrese el monto que va a pagar (solo numeros): "
	Leer monto_ingresado
	
	Mientras monto_ingresado <> valor_estacionamiento Hacer
		//primer bloque de codigo
		Imprimir "El monto ingresado no es es correcto. La barrera no se levantara. Debe ingresar $1000."
		Imprimir "Ingrese nuevamente el monto a pagar: "
		Leer monto_ingresado
	Fin Mientras
	
	Imprimir "El monto ingresado es correcto. Muchas gracias. La barrera se levantara."
	
FinAlgoritmo
