Algoritmo SI_SINO_estacionamiento
	
	Definir monto_ingresado, valor_estacionamiento Como Entero
	
	valor_estacionamiento = 1000
	
	Imprimir "Bienvenido al estacionamiento del Info. El valor del estacionamiento es de $1000."
	Imprimir "Por favor ingrese el monto que va a pagar (solo numeros): "
	Leer monto_ingresado
	
	Si monto_ingresado = valor_estacionamiento Entonces
		Imprimir "Muchas gracias. Ahora la barrera se levantara y usted puede ingresar."
	SiNo
		Imprimir "Disculpe pero el monto ingresado es incorrecto. La barrera no se levantara por lo que usted no puede pasar."
		
	FinSi
	
FinAlgoritmo
