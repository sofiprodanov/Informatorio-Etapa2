Algoritmo retiro_dinero_banco
	
	//Ej 3: Simulacion de retiro de dinero en un banco
	
	Definir saldo, retiro Como Entero
	
	saldo = 50000
	
	Escribir "Indica el monto a retirar (solo numeros): "
	Leer retiro
	
	Si retiro <= saldo Entonces
		Imprimir "Procesando extraccion."
	SiNo
		Imprimir "Fondos insuficientes."
	Fin Si
	
FinAlgoritmo
