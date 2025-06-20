Algoritmo registracion_iva
	
	//El sistema de registración de IVA debe asignar la letra a un comprobante de venta. 
	//Para ello se debe tener en cuenta que la empresa emisora del comprobante emite comprobantes ´C´ en el caso que la misma 
	//revista el carácter de Responsable No Inscripto (RNI), Monotributista (M) o Exento (E), 
	//cualquiera sea el carácter fiscal del comprador. Si la empresa emisora es Responsable Inscripto (RI), 
	//emitirá un comprobante ´A´ si el comprador es RI o es RNI, pero emitirá un comprobante ´B´ si el comprador es M o E.
	
	Definir empresa_emisora, comprador, comprobante Como Caracter
	Definir op1, op2 Como Entero
	
	Repetir // define caracter fiscal de la empresa
		Escribir "Para poder clasificar el comprobante de venta requiero que me indiques si tu empresa es:"
		Escribir "1. RNI, M o E"
		Escribir "2. RI"
		Leer op1
		
		Segun op1 Hacer
			1:
				empresa_emisora = "RNI, M o E"
			2:
				empresa_emisora = "RI"
			De Otro Modo:
				Escribir "Opcion no valida."
		Fin Segun
		
	Hasta Que (op1 = 1) o (op1 = 2) 
	
	Repetir // define caracter fiscal del comprador
		Escribir "¿Cual es el caracter fiscal del comprador?"
		Escribir "1. RI o RNI"
		Escribir "2. M o E"
		Leer op2
		
		Segun op2 Hacer
			1:
				comprador = "RI o RNI"
			2:
				comprador = "M o E"
			De Otro Modo:
				Escribir "Opcion no valida."
		Fin Segun
		
	Hasta Que (op2 = 1) o (op2 = 2) 
	
	// empresa emisora es RNI, M o E, va a emitir comprobante C para el comprador (sin importar caracter fiscal)
	// empresa emisora es RI, va a emitir comprobante A si el comprador es RI o RNI
	// empresa emisora es RI, va a emitir comprobante B si el comprador es M o E
	
	Si empresa_emisora = "RI" y comprador = "RI o RNI" Entonces // indicar el tipo de factura s/el caracter fiscal de la empresa emisora y el comprador
		Escribir "Se emitira factura A para el comprador."
	SiNo
		Si empresa_emisora = "RI" y comprador = "M o E" Entonces
			Escribir "Se emitira factura B para el comprador."
		Sino 
			Escribir "Se emitira factura C para el comprador."
		FinSi
	FinSi
		
FinAlgoritmo
