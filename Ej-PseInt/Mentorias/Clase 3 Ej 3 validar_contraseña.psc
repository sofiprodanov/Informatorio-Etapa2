Algoritmo validar_contrase�a
	
	Definir password Como Caracter
	
	Escribir "Ingresa la contrase�a: "
	Leer password
	
	Mientras password <> "1234" Hacer
		//Escribir el mensaje que se va a Repetir
		Escribir "Contrase�a incorrecta. Intente nuevamente."
		//Para que salga el input para completar nuevamente la contrase�a
		Leer password
	Fin Mientras
	
	Escribir "Acceso concedido."
	
FinAlgoritmo
